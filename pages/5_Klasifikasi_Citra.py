import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

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

     /* File uploader background & teks */
    div[data-testid="stFileUploader"] {
        background-color: white;
        color: black;
    }

    /* Placeholder text (abu-abu) */
    div[data-testid="stFileUploader"] p {
        color: black;
    }

    /* Tombol 'Browse files' */
    div[data-testid="stFileUploader"] button {
        background-color: #f0f0f0;
        color: black;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# Load model
@st.cache_resource
def load_model():
    model = tf.keras.models.load_model("model/model_skenario6_fold1.h5")
    return model

model = load_model()

# Label kelas
class_names = ['bercakdaun', 'keriting', 'sehat']

st.title("📷 Klasifikasi Citra Daun Cabe")

uploaded_file = st.file_uploader("Unggah gambar daun cabe 🌿", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Gambar yang diunggah", width=100)

    # Preprocessing
    image = image.resize((299, 299))
    img_array = tf.keras.preprocessing.image.img_to_array(image)
    img_array = tf.expand_dims(img_array, 0) / 255.0  # Normalisasi

    # Prediksi
    prediction = model.predict(img_array)
    predicted_class = class_names[np.argmax(prediction)]

    st.markdown(f"### ✅ Prediksi: **{predicted_class}**")
    st.bar_chart(prediction[0])
