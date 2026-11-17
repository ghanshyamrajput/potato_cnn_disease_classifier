
import streamlit as st
import tensorflow as tf
import numpy as np
from PIL import Image

st.set_page_config(page_title="Potato Disease", page_icon="🥔")

@st.cache_resource
def load_model():
    return tf.keras.models.load_model("potato_cnn_model.keras")

st.title("🥔 Potato Leaf Disease Detection")
st.subheader("AI Based Plant Disease Detection")
st.write("Upload a potato leaf image to detect disease.")

uploaded_file = st.file_uploader(
    "Upload Potato Leaf Image",
    type=["jpg", "jpeg", "png"]
)

class_names = ["Early Blight", "Late Blight", "Healthy"]

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")
    st.image(image, caption="Uploaded Leaf", width=200)

    if st.button("Predict Disease"):
        try:
            model = load_model()

            img = image.resize((128, 128))
            arr = np.array(img)
            arr = np.expand_dims(arr, axis=0)

            prediction = model.predict(arr)[0]

            index = np.argmax(prediction)
            disease = class_names[index]

            st.subheader("📊 Prediction Result")

            if disease == "Healthy":
                st.success("🌱 Potato Leaf is Healthy")
            else:
                st.error("⚠️ Disease Detected: " + disease)

            st.write("### Class Confidence")

            for i in range(3):
                score = float(prediction[i]) * 100
                st.write(class_names[i], f"{score:.2f}%")
                st.progress(score / 100)

        except Exception as e:
            st.error(f"Error: {e}")

else:
    st.info("Please upload a potato leaf image first.")
