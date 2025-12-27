import streamlit as st
from rembg import remove
from PIL import Image, ImageOps
import io

st.set_page_config(page_title="AI Studio Pro", layout="wide")

st.title("📸 Professional AI Photo Editor")
st.write("Upload karein aur professional edits payein!")

uploaded_file = st.file_uploader("Photo choose karein...", type=["jpg", "jpeg", "png"])

if uploaded_file:
    col1, col2 = st.columns(2)
    img = Image.open(uploaded_file)
    
    with col1:
        st.header("Original")
        st.image(img, use_container_width=True)

    # Tool Options
    option = st.selectbox("Action select karein:", 
                         ["Background Hatayein", "White Background (Marketplace)", "Blur Background"])

    if st.button("Process Karein"):
        with st.spinner("AI kaam kar raha hai..."):
            if option == "Background Hatayein":
                result = remove(img)
            elif option == "White Background (Marketplace)":
                no_bg = remove(img)
                result = Image.new("RGB", no_bg.size, (255, 255, 255))
                result.paste(no_bg, mask=no_bg.split()[3])
            
            with col2:
                st.header("Result")
                st.image(result, use_container_width=True)
                
                # Download Button
                buf = io.BytesIO()
                result.save(buf, format="PNG")
                st.download_button("Download Image", buf.getvalue(), "edited.png")
