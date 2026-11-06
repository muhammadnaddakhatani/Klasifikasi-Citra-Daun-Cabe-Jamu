import streamlit as st
from PIL import Image

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
PENGUJIAN_DIR = BASE_DIR / "img" / "pengujian"

st.set_page_config(layout="wide")

st.markdown(
    """
    <style>
    /* Background utama */
    .stApp {
        background-color: white;
        color: black;
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

    /* Hilangkan header hitam */
    header[data-testid="stHeader"] {
        display: none;
    }

    /* Container gambar */
    img {
        background-color: white;
    }

    /* Hilangkan bayangan hitam */
    .stImage > img {
        background-color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("Hasil Pengujian Model Setiap Skenario")

# --- Tabs Skenario ---
tabs = st.tabs([
    "Skenario 1", "Skenario 2", "Skenario 3",
    "Skenario 4", "Skenario 5", "Skenario 6"
])

# =====================================
# === Learning Rate & Batch Size Tiap Skenario
# =====================================

config_skenario = {
    1: {"lr": 0.01, "ep": 30},
    2: {"lr": 0.01, "ep": 50},
    3: {"lr": 0.001,  "ep": 30},
    4: {"lr": 0.001, "ep": 50},
    5: {"lr": 0.0001, "ep": 30},
    6: {"lr": 0.0001, "ep": 50},
}

# ==========================
# ==== TEMPLATE SKENARIO ===
# ==========================

def tampilkan_skenario(tabs_obj, nomor_skenario, grafik_paths):
    with tabs_obj[nomor_skenario - 1]:

        # ambil konfigurasi sesuai skenario
        lr = config_skenario[nomor_skenario]["lr"]
        ep = config_skenario[nomor_skenario]["ep"]

        st.markdown(f"## **Skenario {nomor_skenario}**")
        st.write(
            f"Pada Skenario {nomor_skenario} dilakukan dengan menggunakan "
            f"**Learning Rate {lr}**, **Epoch {ep}**, **BatchSize 32**."
        )

        st.write("Berikut ini adalah grafik dari Fold 1 sampai Fold 5:")

        # tampilkan gambar satu per satu secara vertikal
        for i, img_path in enumerate(grafik_paths):
            st.markdown(f"### Grafik Pengujian Fold {i+1}")

            img = Image.open(img_path)
            st.image(img, width=300)

            st.markdown("---")


# ===============================
# ==== DAFTAR GAMBAR SKENARIO ===
# ===============================

grafik_skenario1 = [
    PENGUJIAN_DIR / "skenario1" / "fold 1.png",
    PENGUJIAN_DIR / "skenario1" / "fold 2.png",
    PENGUJIAN_DIR / "skenario1" / "fold 3.png",
    PENGUJIAN_DIR / "skenario1" / "fold 4.png",
    PENGUJIAN_DIR / "skenario1" / "fold 5.png",
]

grafik_skenario2 = [
    PENGUJIAN_DIR / "skenario2" / "fold 1.png",
    PENGUJIAN_DIR / "skenario2" / "fold 2.png",
    PENGUJIAN_DIR / "skenario2" / "fold 3.png",
    PENGUJIAN_DIR / "skenario2" / "fold 4.png",
    PENGUJIAN_DIR / "skenario2" / "fold 5.png",
]

grafik_skenario3 = [
    PENGUJIAN_DIR / "skenario3" / "fold 1.png",
    PENGUJIAN_DIR / "skenario3" / "fold 2.png",
    PENGUJIAN_DIR / "skenario3" / "fold 3.png",
    PENGUJIAN_DIR / "skenario3" / "fold 4.png",
    PENGUJIAN_DIR / "skenario3" / "fold 5.png",
]

grafik_skenario4 = [
    PENGUJIAN_DIR / "skenario4" / "fold 1.png",
    PENGUJIAN_DIR / "skenario4" / "fold 2.png",
    PENGUJIAN_DIR / "skenario4" / "fold 3.png",
    PENGUJIAN_DIR / "skenario4" / "fold 4.png",
    PENGUJIAN_DIR / "skenario4" / "fold 5.png",
]

grafik_skenario5 = [
    PENGUJIAN_DIR / "skenario5" / "fold 1.png",
    PENGUJIAN_DIR / "skenario5" / "fold 2.png",
    PENGUJIAN_DIR / "skenario5" / "fold 3.png",
    PENGUJIAN_DIR / "skenario5" / "fold 4.png",
    PENGUJIAN_DIR / "skenario5" / "fold 5.png",
]

grafik_skenario6 = [
    PENGUJIAN_DIR / "skenario6" / "fold 1.png",
    PENGUJIAN_DIR / "skenario6" / "fold 2.png",
    PENGUJIAN_DIR / "skenario6" / "fold 3.png",
    PENGUJIAN_DIR / "skenario6" / "fold 4.png",
    PENGUJIAN_DIR / "skenario6" / "fold 5.png",
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
