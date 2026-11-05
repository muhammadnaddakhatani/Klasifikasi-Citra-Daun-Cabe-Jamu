import streamlit as st
from PIL import Image
import os

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

st.title("Preprocessing Dataset")

BASE_DIR = r"E:/SKRIPSI/streamlit/preprocessing/"
KELAS = ["bercakdaun", "keriting", "sehat"]


# ============================
# Fungsi scan gambar per kelas
# ============================
def load_images_per_class(folder):
    folder_path = os.path.join(BASE_DIR, folder)

    if not os.path.exists(folder_path):
        st.warning(f"Folder {folder} tidak ditemukan.")
        return {}

    hasil = {}

    for cls in KELAS:
        class_dir = os.path.join(folder_path, cls)
        if not os.path.exists(class_dir):
            hasil[cls] = []
            continue

        imgs = [
            os.path.join(class_dir, f)
            for f in os.listdir(class_dir)
            if f.lower().endswith((".jpg", ".png", ".jpeg"))
        ]
        hasil[cls] = imgs

    return hasil


# ============================
# Fungsi tampil grid
# ============================
def show_grid(images, cols=6):
    if not images:
        st.info("Tidak ada gambar ditemukan.")
        return

    rows = (len(images) + cols - 1) // cols
    index = 0

    for _ in range(rows):
        columns = st.columns(cols)
        for col in columns:
            if index < len(images):
                img = Image.open(images[index])
                col.image(img, use_column_width=True)
                col.caption(os.path.basename(images[index]))
                index += 1


# ============================
# TABS PREPROCESSING
# ============================
tab1, tab2, tab3 = st.tabs(["Augmentasi", "Bounding Box", "Resize"])


# ============================
# TAB AUGMENTASI
# ============================
with tab1:
    st.subheader("Augmentasi")

    data = load_images_per_class("augmentasi")

    for cls in KELAS:
        st.markdown(f"### {cls.capitalize()}")
        show_grid(data[cls])
        st.markdown("---")


# ============================
# TAB BOUNDING BOX
# ============================
with tab2:
    st.subheader("Bounding Box")

    data = load_images_per_class("bounding_box")

    for cls in KELAS:
        st.markdown(f"### {cls.capitalize()}")
        show_grid(data[cls])
        st.markdown("---")


# ============================
# TAB RESIZE
# ============================
with tab3:
    st.subheader("Resize")

    data = load_images_per_class("resize")

    for cls in KELAS:
        st.markdown(f"### {cls.capitalize()}")
        show_grid(data[cls])
        st.markdown("---")
