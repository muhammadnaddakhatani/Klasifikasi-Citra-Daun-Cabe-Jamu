import streamlit as st

# --- Judul halaman ---
st.markdown(
    "<h1 style='text-align: center;'>Dataset</h1>",
    unsafe_allow_html=True
)

st.markdown("""
<style>
html, body, [data-testid="stApp"] {
    background-color: white !important;
}

[data-testid="stAppViewContainer"] {
    background-color: white !important;
    padding-top: 0px !important;
}

/* Hilangkan header hitam */
header[data-testid="stHeader"] {
    display: none;
}

/* Sidebar abu terang */
[data-testid="stSidebar"] {
    background-color: #f5f5f5 !important;
}

/* Semua teks hitam */
* {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

# --- Deskripsi dataset ---
deskripsi = """
Dataset yang digunakan dalam penelitian ini adalah daun cabe jamu sebagai data input 
adalah citra RGB yang di dalamnya terdapat gambar daun cabe jamu dengan jumlah total 
384 gambar. Data daun cabe jamu diklasifikasikan menjadi 3 kelas yaitu Mosaic Virus 
(virus keriting), Yellow Virus (virus kuning) dan daun sehat. Dataset tersebut merupakan 
data primer yang diambil secara langsung diperoleh secara langsung dari perkebunan petani di Desa Kebunan, Kecamatan Kota Sumenep dan Desa Aengbaja Kenek, Kecamatan Bluto. 
Pengambilan data dilakukan menggunakan kamera handphone beresolusi 12 MP pada pukul 09.00 – 11.30 WIB dengan jarak sekitar 15 cm dari objek dan di mulai pada tanggal 16 Agustus 2023 dan 3 Februari 2025. Gambar tersebut diambil dengan perlakuan khusus pada 
saat pengambilan foto, yaitu dengan meletakkan kertas putih di belakang daun cabe jamu agar data 
tersebut dapat mudah diklasifikasikan.
"""

st.markdown(
    f"<p style='text-align: justify; font-size: 16px;'>{deskripsi}</p>",
    unsafe_allow_html=True
)

st.markdown("---")

# --- Kalimat pengantar ---
st.markdown(
    "<p style='text-align: center; font-size: 16px;'>Berikut ini adalah contoh beberapa "
    "gambar dari setiap kelas</p>",
    unsafe_allow_html=True
)

st.markdown("")

# ============================================================
#               BAGIAN TAMPILAN GAMBAR PER KELAS
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.image("E:/SKRIPSI/streamlit/img/bercakdaun.jpg", caption="Bercak Daun", use_column_width=True)

with col2:
    st.image("E:/SKRIPSI/streamlit/img/keriting.jpg", caption="Keriting", use_column_width=True)

with col3:
    st.image("E:/SKRIPSI/streamlit/img/sehat.jpg", caption="Sehat", use_column_width=True)




