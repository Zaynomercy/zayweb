import streamlit as st
from PIL import Image

st.title("Aplikasi Menu Test Zay")

menu = st.sidebar.selectbox("Pilih Menu", ["Home", "Tentang", "Kontak"])

if menu == "Home":
    st.header("Selamat Datang di Halaman Home!")
    st.write("Ini adalah halaman utama dari aplikasi.")
    
    image = Image.open("ciko.jpg")
    st.image(image, caption="Halo, ini saya!", use_column_width=True)

elif menu == "Tentang":
    st.header("Tentang Aplikasi")
    st.write("Aplikasi ini dibuat menggunakan Streamlit, Spyder, Python3, VSCode.")
    st.write("Tujuannya untuk saya belajar pemrogramman.")

elif menu == "Kontak":
    st.header("Hubungi Kami")
    st.write("📧 Email: vizaysemangat30@gmail.com")
    st.write("📷 Instagram: @vizaysemangat")
