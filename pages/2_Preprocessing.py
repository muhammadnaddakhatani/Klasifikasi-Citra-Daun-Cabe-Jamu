import streamlit as st
from PIL import Image
from pathlib import Path

# ============================
# KONFIGURASI DIREKTORI
# ============================
BASE_DIR = Path(__file__).resolve().parent.parent
PREPROCESSING_DIR = BASE_DIR / "preprocessing"

KELAS = ["bercakdaun", "keriting", "sehat"]

# ============================
# CUSTOM CSS
# ============================
st.markdown("""
<style>
html, body, [data-testid="stApp"] {
    background-color: white !important;
}

[data-testid="stAppViewContainer"] {
    background-color: white !important;
    padding-top: 0px !important;
}

header[data-testid="stHeader"] {
    display: none;
}

[data-testid="stSidebar"] {
    background-color: #f5f5f5 !important;
}

* {
    color: black !important;
}
</style>
""", unsafe_allow_html=True)

st.title("Preprocessing Dataset")


# ============================
# FUNGSI SCAN GAMBAR PER KELAS
# ============================
def load_images_per_class(folder):

    folder_path = PREPROCESSING_DIR / folder

    # Inisialisasi dictionary agar semua kelas tersedia
    hasil = {cls: [] for cls in KELAS}

    if not folder_path.exists():
        st.warning(
            f"Folder {folder} tidak ditemukan: {folder_path}"
        )
        return hasil

    if not folder_path.is_dir():
        st.warning(f"{folder_path} bukan sebuah folder.")
        return hasil

    for cls in KELAS:

        class_dir = folder_path / cls

        if not class_dir.exists():
            continue

        imgs = [
            str(file)
            for file in class_dir.iterdir()
            if file.is_file()
            and file.suffix.lower() in (".jpg", ".png", ".jpeg")
        ]

        hasil[cls] = sorted(imgs)

    return hasil


# ============================
# FUNGSI TAMPIL GRID
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

                try:
                    with Image.open(images[index]) as img:
                        col.image(
                            img.copy(),
                            use_container_width=True
                        )

                    col.caption(Path(images[index]).name)

                except Exception as e:
                    col.error(
                        f"Gagal membaca gambar: {Path(images[index]).name}"
                    )

                index += 1


# ============================
# TABS PREPROCESSING
# ============================
tab1, tab2, tab3 = st.tabs([
    "Augmentasi",
    "Bounding Box",
    "Resize"
])


# ============================
# TAB AUGMENTASI
# ============================
with tab1:

    st.subheader("Augmentasi")

    data = load_images_per_class("augmentasi")

    for cls in KELAS:

        st.markdown(f"### {cls.capitalize()}")

        show_grid(data.get(cls, []))

        st.markdown("---")


# ============================
# TAB BOUNDING BOX
# ============================
with tab2:

    st.subheader("Bounding Box")

    data = load_images_per_class("bounding_box")

    for cls in KELAS:

        st.markdown(f"### {cls.capitalize()}")

        show_grid(data.get(cls, []))

        st.markdown("---")


# ============================
# TAB RESIZE
# ============================
with tab3:

    st.subheader("Resize")

    data = load_images_per_class("resize")

    for cls in KELAS:

        st.markdown(f"### {cls.capitalize()}")

        show_grid(data.get(cls, []))

        st.markdown("---")
