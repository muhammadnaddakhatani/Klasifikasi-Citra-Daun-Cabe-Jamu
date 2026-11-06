import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image
from pathlib import Path


# ============================================================
# KONFIGURASI DIREKTORI
# ============================================================

BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "model" / "model_skenario6_fold1.h5"


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>
    .stApp {
        background-color: white;
        color: black;
    }

    section[data-testid="stSidebar"] {
        background-color: white;
    }

    div[data-testid="stVerticalBlock"] {
        background-color: transparent;
    }

    * {
        color: black !important;
    }

    header[data-testid="stHeader"] {
        display: none;
    }

    img {
        background-color: white;
    }

    .stImage > img {
        background-color: white;
    }

    div[data-testid="stFileUploader"] {
        background-color: white;
        color: black;
    }

    div[data-testid="stFileUploader"] p {
        color: black;
    }

    div[data-testid="stFileUploader"] button {
        background-color: #f0f0f0;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# LOAD MODEL
# ============================================================

@st.cache_resource
def load_model():

    if not MODEL_PATH.exists():
        st.error(f"Model tidak ditemukan: {MODEL_PATH}")
        st.stop()

    model = tf.keras.models.load_model(str(MODEL_PATH))

    return model


model = load_model()


# ============================================================
# LABEL KELAS
# ============================================================

class_names = ['bercakdaun', 'keriting', 'sehat']


# ============================================================
# TAMPILAN HALAMAN
# ============================================================

st.title("📷 Klasifikasi Citra Daun Cabe")

uploaded_file = st.file_uploader(
    "Unggah gambar daun cabe 🌿",
    type=["jpg", "png", "jpeg"]
)


# ============================================================
# PROSES KLASIFIKASI
# ============================================================

if uploaded_file is not None:

    try:

        image = Image.open(uploaded_file).convert("RGB")

        st.image(
            image,
            caption="Gambar yang diunggah",
            width=100
        )

        # Preprocessing
        image = image.resize((299, 299))

        img_array = tf.keras.preprocessing.image.img_to_array(image)

        img_array = tf.expand_dims(img_array, 0) / 255.0

        # Prediksi
        prediction = model.predict(img_array)

        predicted_class = class_names[np.argmax(prediction)]

        # Hasil prediksi
        st.markdown(
            f"### ✅ Prediksi: **{predicted_class}**"
        )

        st.bar_chart(
            prediction[0],
            x_label="Kelas",
            y_label="Probabilitas"
        )

    except Exception as e:

        st.error(f"Terjadi kesalahan saat klasifikasi: {e}")
