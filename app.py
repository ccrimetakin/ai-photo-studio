import streamlit as st
from rembg import remove
from PIL import Image, ImageOps, ImageFilter
import io

st.set_page_config(page_title="AI Studio Pro", layout="wide")

st.title("🚀 All-in-One AI Photo Studio")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    img = Image.open(uploaded_file)
    
    # Sidebar for Tools like Photoroom
    st.sidebar.header("Classics & Tools")
    tool = st.sidebar.radio("Select Tool", 
        ["Background Remover", "Blur Effect", "Black & White", "Marketplace Resize"])

    if st.button("Apply Magic"):
        with st.spinner("Processing..."):
            if tool == "Background Remover":
                output = remove(img)
                st.image(output, caption="Transparent Background")
            
            elif tool == "Blur Effect":
                output = img.filter(ImageFilter.GaussianBlur(10))
                st.image(output, caption="Blur Applied")

            elif tool == "Black & White":
                output = ImageOps.grayscale(img)
                st.image(output, caption="B&W Classic")

            elif tool == "Marketplace Resize":
                # Resizing for Shopify/Amazon (Square)
                output = ImageOps.pad(img, (1080, 1080), color="white")
                st.image(output, caption="1080x1080 Square Template")

            # Download Option
            buf = io.BytesIO()
            if tool == "Background Remover":
                output.save(buf, format="PNG")
            else:
                output.save(buf, format="JPEG")
            st.download_button("Download Result", buf.getvalue(), "edited_image.png")
