import streamlit as st

uploaded_image = st.file_uploader(label="Choose a file", type=['png', 'jpg', 'jpeg'])
if uploaded_image:
  st.image(uploaded_image.getvalue())
