
import streamlit as st
from PIL import Image

st.title('Control Brightness')

uploaded_file = st.file_uploader("Selecct Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    
    slider_val = st.slider(
            ' dark <---> brigh ', 
            value=1.0,
            min_value=0.0,
            max_value=2.0,
            step=0.1
            ) 
    
    enhanced_img = image.point(lambda p: p * slider_val)  

    st.image(enhanced_img, caption="Uploaded", use_column_width=True)


