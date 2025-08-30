from PIL import Image
import io

def load_image(uploaded_file) -> Image.Image:
    image = Image.open(uploaded_file).convert("RGB")
    return image
