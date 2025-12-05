# import library
import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

# dataset utama
suhu = [25, 26, 27, 28, 29, 30, 31, 32, 33, 34]
penjualan = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200]

# dataset tambahan (data penjualan)
penjualan_weekdays = [100, 120, 130, 140, 150, 160, 170, 180, 190, 200]
penjualan_weekends = [50, 60, 70, 80, 90, 100, 110, 120, 130, 140]

# data untuk analisis
data = {
    'suhu' : [25, 26, 27, 28, 29, 30, 31, 32, 33, 34],
    'penjualan_cokelat' : [40, 45, 50, 55, 60, 65, 70, 75, 80, 90],
    'penjualan_vanila' : [82, 80, 78, 76, 77, 80, 82, 85, 88, 90],
    'penjualan_stroberi' : [55, 50, 55, 60, 65, 60, 65, 70, 72, 90],
    'kelembapan' : [70, 75, 80, 85, 90, 95, 100, 105, 110, 115]
}
# konversi data dataframe
df = pd.DataFrame(data)

# layout utama
st.title('visualisasi scatter plot Penjualan Es Krim')
st.sidebar.header("Pengaturan Visualisasi")

# menu di sidebar
option = st.sidebar.selectbox(
    "pilih contoh Scatter Plot",
    (
        "Basic Scatter Plot", 
        "Kustomisasi Scatter Plot",
        "Multiple Scatter Plot",
        "Analisis Scatter Plot"
    )
)

# identitas kelompok
st.caption("Praktikum 5 - Matplotlib Scatter Plot")
st.markdown("""
Kelompok 29
- Amirullah (0110222106)
- Indah Agustin (0110222250)
- Miftahul Jannah (0110222101)           
"""  )

# 1 BASIC SCATTER PLOT
def basic_scatter():
    st.subheader("Basic Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es Krim dengan suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    st.pyplot(fig)

# 2 KUSTOMISASI SCATTER PLOT
def custom_scatter():
    st.subheader("Kustomisasi Scatter Plot")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='purple', s=100, edgecolors='black', alpha=0.7)
    ax.set_title('Hubungan Penjualan Es Krim dengan suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)

# 3 MULTIPLE SCATTER PLOT
def multiple_scatter():
    st.subheader("3. MULTIPLE SCATTER PLOT")
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan_weekdays, color='green', label="Hari Kerja", s=80)
    ax.scatter(suhu, penjualan_weekends, color='lime', label="Akhir Pekan", s=80)
    ax.set_title('Hubungan Penjualan Es Krim dengan suhu')
    ax.set_xlabel('Suhu')
    ax.set_ylabel('Penjualan Es Krim')
    ax.grid(True)
    st.pyplot(fig)


# 4 ANALISIS DENGAN SCATTER PLOT
def scatter_3_variabel():
    st.subheader("4. ANALISIS DENGAN SCATTER PLOT")

    #opsi jenis es krim
    jenis_eskrim = st.selectbox('pilih Jenis Es Krim', ['Cokelat', 'Vanila', 'Stroberi'])
    # logika untuk opsi jenis eskrim berdasarkan pilihan
    if jenis_eskrim == 'Cokelat' :
        penjualan = df['penjualan_cokelat']
    elif jenis_eskrim == 'Vanila' :
        penjualan = df['penjualan vanila']
    else:
        penjualan = df['penjualan stroberi']

    st.subheader("Data Penjualan dan Suhu")
    st.dataframe(df)

    # scatter plot
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['suhu'], penjualan, c=df['kelembapan'], s=100, cmap='coolwarm', alpha=0.7)

    # styling
    ax.set_title(f'Hubungan Penjualan {jenis_eskrim} vs Suhu dan Kelembapan')
    ax.set_xlabel('Suhu')
    ax.set_ylabel(f'Penjualan Es Krim {jenis_eskrim}')
    fig.colorbar(scatter, label='Kelmbapan (%)')

    st.pyplot(fig)

    # ringkasan hubungan
    st.subheader('Analisis Hubungan')
    st.write(f'Grafik menunjukkan hubungan anatara suhu, kelembapan, dan penjualan eskrim jenis **{jenis_eskrim}**')

# Routing berdasarkan menu sidebar
if option == "Basic Scatter Plot" :
    basic_scatter()
elif option == "Kustomisasi Scatter Plot" :
    custom_scatter()
elif option == "Multiple Scatter Plot" :
    multiple_scatter()
elif option == "Analisis Scatter Plot" :
    scatter_3_variabel()