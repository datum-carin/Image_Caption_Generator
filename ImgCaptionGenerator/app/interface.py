import streamlit as st
from app.model import CaptionGenerator
from app.utils import load_image

def run_app():
    st.title("🖼️ Image Caption Generator")
    st.write("Upload an image and get a caption using BLIP.")

    uploaded_file = st.file_uploader("Choose an image", type=["jpg", "jpeg", "png"])

    if uploaded_file:
        image = load_image(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        generator = CaptionGenerator()
        caption = generator.generate_caption(image)
        st.success(f"📝 Caption: {caption}")
