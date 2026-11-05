import streamlit as st


st.set_page_config(page_title="Cover Skripsi", layout="wide")  # gunakan mode wide

# CSS: full width & teks besar
st.markdown("""
<style>
html, body, [data-testid="stApp"] {
    background-color: white !important;
}

[data-testid="stAppViewContainer"] {
    background-color: white !important;
    padding-top: 0px !important;
}

[data-testid="stSidebar"] {
    background-color: #f5f5f5 !important;
}

header[data-testid="stHeader"] {
    display: none;
}

.block-container {
    padding-top: 1rem !important;
    padding-bottom: 1rem !important;
    padding-left: 0rem !important;
    padding-right: 0rem !important;
    max-width: 100% !important;
}

* {
    color: black !important;
}

.center {
    text-align: center;
}

.judul {
    font-weight: bold;
    font-size: 32px;
    margin-top: 50px;
}

.subjudul {
    font-style: italic;
    font-size: 22px;
    margin-bottom: 30px;
    line-height: 1.6;
}

.nama {
    font-weight: bold;
    text-decoration: underline;
    font-size: 20px;
    margin-bottom: 10px;
}

.info {
    font-size: 18px;
    margin-bottom: 8px;
}

.footer {
    font-size: 18px;
    margin-top: 60px;
}
</style>
""", unsafe_allow_html=True)



# --- JUDUL UTAMA ---
st.markdown("<p class='center judul'>PROPOSAL SKRIPSI</p>", unsafe_allow_html=True)
st.markdown("<p class='center subjudul'>KLASIFIKASI PENYAKIT PADA DAUN CABE JAMU<br>MENGGUNAKAN METODE <i>INCEPTIONV3</i></p>", unsafe_allow_html=True)

# --- LOGO (digeser sedikit biar pas tengah huruf) ---
col1, col2, col3 = st.columns([4, 3, 3.5])
with col2:
    st.image("img/utm.jpg", width=260)  # perbesar logo

# --- IDENTITAS ---
st.markdown("""
<div class="center info">
    <p>Oleh:</p>
    <p class="nama">MUHAMMAD NADDA KHATANI</p>
    <p>210411100069</p>
</div>
""", unsafe_allow_html=True)

# --- DOSEN PEMBIMBING ---
st.markdown("""
<div class="center info">
    <p>Dosen Pembimbing 1 : Prof. Dr. <b>Eva Mala Sari, S.Kom., M.Kom.</b></p>
    <p>Dosen Pembimbing 2 : Prof. Dr. <b>Jeri Bactiar, S.T., M.T.</b></p>
</div>
""", unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("""
<div class="center footer">
    <p><b>PROGRAM STUDI TEKNIK INFORMATIKA</b><br>
    JURUSAN TEKNIK INFORMATIKA<br>
    FAKULTAS TEKNIK<br>
    UNIVERSITAS TRUNOJOYO MADURA<br>
    2025</p>
</div>
""", unsafe_allow_html=True)
