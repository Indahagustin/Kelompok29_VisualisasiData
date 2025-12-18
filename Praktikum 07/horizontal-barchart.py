import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# judul
st.title("Praktikum 7 Visualisasi Data")
st.subheader("Horizontal Bar Chart & Stacked Horizontal Bar Chart")

# identitas kelompok
st.markdown("""
- Amirullah (0110222106)
- Indah Agustin (0110222250)
- Miftahul Jannah (0110222101)           
"""  )

# dataset
brands = ['Brands A', 'Brands B', 'Brand C', 'Brand D']
sales_2023 = [350, 420, 300, 280]
sales_2024 = [380, 450, 320, 300]

# atur posisi Y
y = np.arange(len(brands))
bar_width = 0.4


# filter kategori
kategori = st.selectbox(
    "pilih kategori visualisasi",
    ['Basic Chart', 'Kustomisasi Grafik','Multiple Chart']
)

# basic bar char
if kategori == "Basic Chart":
    st.subheader("Horizontal Bar Chart Sederhana")
    fig1, ax1, = plt.subplots()

    # grafik batang horizontal
    ax1.set_ylabel(y)
    ax1.set_yticklabels(brands)
    ax1.set_title('Horizontal Bar Chart - 2023')
    ax1.set_xlabel('Jumlah Penjualan')
    ax1.set_ylabel('Merk')
    ax1.barh(y, sales_2023, color='Green')
    st.pyplot(fig1)

    # stacked
    st.subheader("Stacked Horizontal Bar Chart Sederhana")
    fig2, ax2, = plt.subplots()
    ax2.set_ylabel(y)
    ax2.set_yticklabels(brands)
    ax2.set_title('Horizontal Bar Chart - 2023')
    ax2.set_xlabel('Jumlah Penjualan')
    ax2.set_ylabel('Merk')
    ax2.barh(y, sales_2023, color='Green', label='2023')
    ax2.barh(y, sales_2024, color='Lime', label='2024', left=sales_2023)
    ax2.legend()
    st.pyplot(fig2)

    # kustomisasi
elif kategori == "Kustomisasi Grafik":
    st.subheader("Kustomisasi Horizontal Bar Chart ")
    fig3, ax3, = plt.subplots()
    ax3.set_ylabel(y)
    ax3.set_yticklabels(brands)
    ax3.set_title('Kustomisasi Horizontal Bar Chart - 2023')
    ax3.set_xlabel('Jumlah Penjualan')
    ax3.set_ylabel('Merk')
    ax3.barh(y, sales_2023, color='red', edgecolor='black')
    ax3.grid(axis='x', linestyle='--', alpha=0.6)
   
   # label nilai
    for i, v in enumerate(sales_2023):
        ax3.text(v + 5, i, str(v), va='center')

    st.pyplot(fig3)
    
    st.subheader("Customized Stacked Horizontal Bar Chart")
    fig4, ax4 = plt.subplots()
    ax4.barh(y, sales_2023, label='2023', color='skyblue', edgecolor='black')
    ax4.barh(y, sales_2024, left=sales_2023, label='2024', color='salmon', edgecolor='black')
    ax4.set_yticks(y)
    ax4.set_yticklabels(brands)
    ax4.set_xlabel("Total Sales (in Units)")
    ax4.set_title("Customized Stacked Sales by Brand")
    ax4.legend()
    ax4.grid(axis='x', linestyle='--', alpha=0.6)

    st.pyplot(fig4)

# multiple chart
else:
    st.subheader('Multiple Horizontal Bar Chart')
    fig5, ax5, = plt.subplots()
    ax5.set_ylabel(y)
    ax5.set_yticklabels(brands)
    ax5.set_title('Multiple  Horizontal Bar Chart - 2023')
    ax5.set_xlabel('Jumlah Penjualan')
    ax5.set_ylabel('Merk')
    ax5.barh(y - bar_width/2, sales_2023, height=bar_width, label='2023')
    ax5.barh(y - bar_width/2, sales_2024, height=bar_width, label='2024')
    ax5.grid(axis='x', linestyle='--', alpha=0.6)
    ax5.legend()
    st.pyplot(fig5)

    st.subheader("Multiple Stacked Horizontal Bar Chart")
    fig6, ax6 = plt.subplots()
    ax6.barh(y, sales_2023, label='2023')
    ax6.barh(y, sales_2024, left=sales_2023, label='2024')
    ax6.set_yticks(y)
    ax6.set_yticklabels(brands)
    ax6.set_xlabel("Total Sales (in Units)")
    ax6.set_title("Multiple Stacked Horizontal Bar Chart")
    ax6.legend()
    st.pyplot(fig6)