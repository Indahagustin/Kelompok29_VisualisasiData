import streamlit as st
import matplotlib.pyplot as plt

# data sample
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10,20,15,25,30,45,40,50,60,55,56,70]
product_B_sales = [5,10,8,15,18,20,22,30,25,35,40,45]

# layout streamlit
st.title("Visualisasi Penjualan Product")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", ("Single Line Plot","Multiple & Customization","Jenis Garis untuk Menunjukan Tren","Subplot"))

# Identitas kelompok
st.caption("Praktikum 3 - Matplotlib Line Chart")
st.markdown("""
- Amirullah (0110222106)
- Indah Agustin (0110222250)
- Miftahul Jannah (0110222101)   
""")

# Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A')
    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    st.pyplot(fig)

# Multiple Line Plot & Customization
def customize_lineplot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', linestyle="--", marker='o', color='blue')
    ax.plot(months, product_B_sales, label='Product B', linestyle="-", marker='x', color='red')

    ax.set_title('Penjualan Produk A per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

# Data sample tambahan
product_C_sales = [8,12,14,18,20,25,28,30,32,35,38,40]
product_D_sales = [12,15,10,18,22,30,25,20,28,32,30,38]
def tren_line_plot():
    fig, axs = plt.subplots()
    axs.plot(months, product_C_sales, label='Product C', linestyle="--", color='green')
    axs.plot(months, product_D_sales, label='Product D', linestyle="-", color='purple')
    axs.set_title('Penjualan Produk C per Bulan')
    axs.set_xlabel('Bulan')
    axs.set_ylabel('Penjualan')
    axs.legend()
    axs.grid(True)
    st.pyplot(fig)


# Subplots
def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

# plot pertama untuk product C
    axs[0].plot(months, product_C_sales, label='Product C', linestyle=":", color='green', marker='d')
    axs[0].set_title('Penjualan Product C per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

# plot pertama untuk product D
    axs[1].plot(months, product_D_sales, label='Product D', linestyle=":", color='purple', marker='s')
    axs[1].set_title('Penjualan Product D per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    plt.show()
    st.pyplot(fig)

# Logika untuk menampilkan visualisasi sesuai menu
if option == "Single Line Plot":
    line_plot()
elif option == "Multiple & Customization":
    customize_lineplot()
elif option == "Jenis Garis untuk Menunjukan Tren":
    tren_line_plot()
elif option == "Subplot":
    subplots()