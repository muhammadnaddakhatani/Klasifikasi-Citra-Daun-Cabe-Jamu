import streamlit as st
from PIL import Image
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PELATIHAN_DIR = BASE_DIR / "img" / "grafik"

# =========================
# KONFIGURASI HALAMAN
# =========================
st.set_page_config(
    layout="wide",
    page_title="Hasil Pelatihan Model"
)

# =========================
# FORCE BACKGROUND PUTIH
# =========================
st.markdown(
    """
    <style>
    /* Background utama */
    .stApp {
        background-color: white;
    }

    /* Hilangkan header hitam */
    header[data-testid="stHeader"] {
        display: none;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: white;
    }

    /* Container default Streamlit */
    div[data-testid="stVerticalBlock"] {
        background-color: transparent;
    }

    /* Semua teks hitam */
    * {
        color: black !important;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# =========================
# JUDUL
# =========================
st.title("Hasil Pelatihan Model Setiap Skenario")

# --- Tabs Skenario ---
tabs = st.tabs([
    "Skenario 1", "Skenario 2", "Skenario 3",
    "Skenario 4", "Skenario 5", "Skenario 6"
])

# =====================================
# === Learning Rate & Epoch Tiap Skenario
# =====================================
config_skenario = {
    1: {"lr": 0.01, "ep": 30},
    2: {"lr": 0.01, "ep": 50},
    3: {"lr": 0.001,  "ep": 30},
    4: {"lr": 0.001, "ep": 50},
    5: {"lr": 0.0001, "ep": 30},
    6: {"lr": 0.0008, "ep": 50},
}

# ==========================
# ==== TEMPLATE SKENARIO ===
# ==========================
def tampilkan_skenario(tabs_obj, nomor_skenario, grafik_paths):
    with tabs_obj[nomor_skenario - 1]:

        lr = config_skenario[nomor_skenario]["lr"]
        ep = config_skenario[nomor_skenario]["ep"]

        st.markdown(f"## **Skenario {nomor_skenario}**")
        st.write(
            f"Pada Skenario {nomor_skenario} dilakukan dengan menggunakan "
            f"**Learning Rate {lr}**, **Epoch {ep}**, **Batch Size 32**."
        )

        st.write("Berikut ini adalah grafik dari Fold 1 sampai Fold 5:")

        for i, img_path in enumerate(grafik_paths):
            st.markdown(f"### Grafik Pelatihan Fold {i+1}")
            img = Image.open(img_path)
            st.image(img, use_column_width=True)
            st.markdown("---")

# ===============================
# ==== DAFTAR GAMBAR SKENARIO ===
# ===============================
grafik_skenario1 = [
    PELATIHAN_DIR / "skenario1"/"fold1.png",
    PELATIHAN_DIR / "skenario1"/"fold2.png",
    PELATIHAN_DIR / "skenario1"/"fold3.png",
    PELATIHAN_DIR / "skenario1"/"fold4.png",
    PELATIHAN_DIR / "skenario1"/"fold5.png",
]

grafik_skenario2 = [
    PELATIHAN_DIR / "skenario2"/"fold1.png",
    PELATIHAN_DIR / "skenario2"/"fold2.png",
    PELATIHAN_DIR / "skenario2"/"fold3.png",
    PELATIHAN_DIR / "skenario2"/"fold4.png",
    PELATIHAN_DIR / "skenario2"/"fold5.png",
]

grafik_skenario3 = [
    PELATIHAN_DIR / "skenario3"/"fold1.png",
    PELATIHAN_DIR / "skenario3"/"fold2.png",
    PELATIHAN_DIR / "skenario3"/"fold3.png",
    PELATIHAN_DIR / "skenario3"/"fold4.png",
    PELATIHAN_DIR / "skenario3"/"fold5.png",
]

grafik_skenario4 = [
    PELATIHAN_DIR / "skenario4"/"fold1.png",
    PELATIHAN_DIR / "skenario4"/"fold2.png",
    PELATIHAN_DIR / "skenario4"/"fold3.png",
    PELATIHAN_DIR / "skenario4"/"fold4.png",
    PELATIHAN_DIR / "skenario4"/"fold5.png",
]

grafik_skenario5 = [
    PELATIHAN_DIR / "skenario5"/"fold1.png",
    PELATIHAN_DIR / "skenario5"/"fold2.png",
    PELATIHAN_DIR / "skenario5"/"fold3.png",
    PELATIHAN_DIR / "skenario5"/"fold4.png",
    PELATIHAN_DIR / "skenario5"/"fold5.png",
]

grafik_skenario6 = [
    PELATIHAN_DIR / "skenario6"/"fold1.png",
    PELATIHAN_DIR / "skenario6"/"fold2.png",
    PELATIHAN_DIR / "skenario6"/"fold3.png",
    PELATIHAN_DIR / "skenario6"/"fold4.png",
    PELATIHAN_DIR / "skenario6"/"fold5.png",
]

# ==========================
# ==== TAMPILKAN SEMUA =====
# ==========================
tampilkan_skenario(tabs, 1, grafik_skenario1)
tampilkan_skenario(tabs, 2, grafik_skenario2)
tampilkan_skenario(tabs, 3, grafik_skenario3)
tampilkan_skenario(tabs, 4, grafik_skenario4)
tampilkan_skenario(tabs, 5, grafik_skenario5)
tampilkan_skenario(tabs, 6, grafik_skenario6)
