import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import re
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
from wordcloud import WordCloud
import io

st.set_page_config(
    page_title="Sentimen Publik terhadap Pemerintah",
    layout="wide"
)

# =====================
# LOAD DATA
# =====================
@st.cache_data
def load_data(path="TRANSLATED-covid-sentiment.csv"):
    df = pd.read_csv(path, low_memory=False)

    # Pastikan kolom tanggal ada dan ubah ke datetime
    if 'date' in df.columns:
        df['datetime'] = pd.to_datetime(df['date'], errors='coerce')
    else:
        # Jika tidak ada kolom 'date', coba kolom 'created_at' atau buat kolom kosong
        if 'created_at' in df.columns:
            df['datetime'] = pd.to_datetime(df['created_at'], errors='coerce')
        else:
            df['datetime'] = pd.NaT

    # Ubah kolom ID besar menjadi string agar aman ditampilkan
    id_cols = [c for c in df.columns if c.endswith('_id')]
    for col in id_cols:
        try:
            df[col] = df[col].astype(str)
        except Exception:
            # fallback: convert via apply(str) jika astype gagal
            df[col] = df[col].apply(lambda x: "" if pd.isna(x) else str(int(x)) if (isinstance(x, float) and x.is_integer()) else str(x))

    # Pastikan kolom tweet ada
    if 'tweet' not in df.columns:
        df['tweet'] = ""

    # Pastikan kolom username ada
    if 'username' not in df.columns:
        df['username'] = ""

    # Pastikan retweets_count & likes_count ada
    if 'retweets_count' not in df.columns:
        df['retweets_count'] = 0
    if 'likes_count' not in df.columns:
        df['likes_count'] = 0

    return df

df = load_data()

# =====================
# CLEAN TEXT
# =====================
def clean_text(text):
    if pd.isna(text):
        return ""
    text = re.sub(r"http\S+", "", str(text))
    text = re.sub(r"@\w+", "", text)
    text = re.sub(r"[^A-Za-z\s]", " ", text)
    return re.sub(r"\s+", " ", text).lower().strip()

df['clean_tweet'] = df['tweet'].apply(clean_text)

# =====================
# SENTIMENT ANALYSIS
# =====================
analyzer = SentimentIntensityAnalyzer()

def get_sentiment(text):
    if not text:
        return "Neutral"
    score = analyzer.polarity_scores(text)['compound']
    if score >= 0.05:
        return "Positive"
    elif score <= -0.05:
        return "Negative"
    else:
        return "Neutral"

df['sentiment'] = df['clean_tweet'].apply(get_sentiment)

# =====================
# SIDEBAR FILTER
# =====================
st.sidebar.title("Filter Data")

# Default date range: if datetime all NaT, fallback to empty selection
min_date = df['datetime'].min()
max_date = df['datetime'].max()
if pd.isna(min_date) or pd.isna(max_date):
    # Provide today's date as fallback to avoid errors in date_input
    min_date = pd.to_datetime("2020-01-01")
    max_date = pd.to_datetime("2020-12-31")

date_range = st.sidebar.date_input(
    "Pilih Rentang Tanggal",
    [min_date.date(), max_date.date()]
)

sentiment_options = sorted(df['sentiment'].unique())
sentiment_filter = st.sidebar.multiselect(
    "Pilih Sentimen",
    sentiment_options,
    default=sentiment_options
)

# Convert date_range to datetimes safely
start_dt = pd.to_datetime(date_range[0])
end_dt = pd.to_datetime(date_range[1])

filtered_df = df[
    (df['datetime'] >= start_dt) &
    (df['datetime'] <= end_dt + pd.Timedelta(days=1) - pd.Timedelta(seconds=1)) &
    (df['sentiment'].isin(sentiment_filter))
].copy()

# =====================
# TITLE
# =====================
st.title("Suara Publik terhadap Kebijakan Pemerintah di Masa COVID-19")
st.write("Visualisasi sentimen dan narasi publik Twitter Indonesia")

# =====================
# METRICS
# =====================
col1, col2, col3 = st.columns(3)
col1.metric("Total Tweet", int(len(filtered_df)))
col2.metric("Total Retweet", int(filtered_df['retweets_count'].sum()) if not filtered_df.empty else 0)
col3.metric("Total Likes", int(filtered_df['likes_count'].sum()) if not filtered_df.empty else 0)

# =====================
# 1. PIE CHART SENTIMENT
# =====================
st.subheader("Distribusi Sentimen Publik")

fig1, ax1 = plt.subplots(figsize=(9, 7))

if filtered_df.empty:
    ax1.text(
        0.5,
        0.5,
        "Tidak ada data untuk rentang tanggal ini",
        ha="center",
        va="center",
        fontsize=12
    )
    ax1.axis("off")
else:
    counts = filtered_df["sentiment"].value_counts()

    wedges, texts, autotexts = ax1.pie(
        counts,
        autopct="%1.1f%%",
        startangle=90,
        colors=sns.color_palette("pastel"),
        pctdistance=0.75,
        labels=None
    )

    ax1.legend(
        wedges,
        counts.index,
        title="Sentimen",
        loc="center left",
        bbox_to_anchor=(1, 0.5)
    )

    ax1.axis("equal")

st.pyplot(fig1, width="stretch")

st.caption(
    "Insight. Sentimen netral sangat dominan, menunjukkan bahwa mayoritas publik menyampaikan informasi atau opini tanpa ekspresi emosional yang kuat. "
    "Sentimen negatif tetap ada, menandakan kritik terhadap kebijakan pemerintah, sementara sentimen positif relatif kecil."
)
# =====================
# 2. LINE CHART TWEET PER HARI
# =====================
st.subheader("Jumlah Tweet per Hari")

fig2, ax2 = plt.subplots(figsize=(8, 4))
if filtered_df.empty or filtered_df['datetime'].isna().all():
    ax2.text(0.5, 0.5, "Tidak ada data tanggal untuk ditampilkan", ha='center', va='center')
    ax2.axis('off')
else:
    tweet_daily = filtered_df.groupby(filtered_df['datetime'].dt.date).size()
    tweet_daily.plot(ax=ax2, marker='o')
    ax2.set_xlabel("Tanggal")
    ax2.set_ylabel("Jumlah Tweet")
    ax2.grid(True, linestyle='--', alpha=0.5)
st.pyplot(fig2, width='stretch')
st.caption("Insight. Puncak aktivitas bisa menjadi indikator respons publik terhadap pengumuman atau kebijakan penting.")

# =====================
# 3. BAR CHART TOP USER
# =====================
st.subheader("Top 10 Akun Paling Aktif")

fig3, ax3 = plt.subplots(figsize=(8, 4))
if filtered_df.empty:
    ax3.text(0.5, 0.5, "Tidak ada data untuk ditampilkan", ha='center', va='center')
    ax3.axis('off')
else:
    top_users = filtered_df['username'].value_counts().head(10)
    sns.barplot(x=top_users.values, y=top_users.index, hue=top_users.index, ax=ax3, palette="viridis", legend=False)
    ax3.set_xlabel("Jumlah Tweet")
    ax3.set_ylabel("Username")
st.pyplot(fig3, width='stretch')
st.caption("Insight. Beberapa akun berperan dominan dalam membentuk narasi.")

# =====================
# 4. HISTOGRAM RETWEET
# =====================
st.subheader("Distribusi Retweet")

fig4, ax4 = plt.subplots(figsize=(8, 4))

if filtered_df.empty:
    ax4.text(
        0.5,
        0.5,
        "Tidak ada data untuk ditampilkan",
        ha="center",
        va="center",
        fontsize=12
    )
    ax4.axis("off")
else:
    retweets = filtered_df["retweets_count"].fillna(0)

    ax4.hist(
        np.log1p(retweets),
        bins=30,
        edgecolor="white"
    )

    ax4.set_xlabel("Jumlah Retweet (Skala Log)")
    ax4.set_ylabel("Frekuensi")

st.pyplot(fig4, width="stretch")

st.caption(
    "Insight. Distribusi retweet sangat timpang. Mayoritas tweet memiliki retweet rendah, "
    "sementara hanya sebagian kecil yang memperoleh retweet tinggi."
)

# =====================
# 5. WORDCLOUD
# =====================
st.subheader("WordCloud Narasi Publik")

fig5, ax5 = plt.subplots(figsize=(10, 4))
if filtered_df.empty or filtered_df['clean_tweet'].str.strip().eq("").all():
    ax5.text(0.5, 0.5, "Tidak ada teks untuk membuat wordcloud", ha='center', va='center')
    ax5.axis('off')
else:
    text = " ".join(filtered_df['clean_tweet'].astype(str).tolist())
    wc = WordCloud(
        width=1600,
        height=800,
        background_color="white",
        collocations=False
    ).generate(text)
    ax5.imshow(wc, interpolation="bilinear")
    ax5.axis("off")
st.pyplot(fig5, width='stretch')
st.caption("Insight. Kata dominan menunjukkan fokus utama opini publik terhadap pemerintah.")

# =====================
# DATA PREVIEW & DOWNLOAD
# =====================
st.subheader("Preview Data")
st.dataframe(
    filtered_df.head(20),
    width='stretch'
)

# Download filtered data as CSV
if not filtered_df.empty:
    csv_buffer = io.StringIO()
    filtered_df.to_csv(csv_buffer, index=False)
    csv_bytes = csv_buffer.getvalue().encode('utf-8')
    st.download_button(
        label="Unduh CSV (filtered)",
        data=csv_bytes,
        file_name="filtered_covid_sentiment.csv",
        mime="text/csv"
    )