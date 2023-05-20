import PIL as Image
import streamlit as st

from detect_tags import detect_objects, get_tags

# local_image_path = "/Users/a81701/code/streamlit/detection/02_物体検出アプリ/sample01.jpg"
# # print(get_tags(local_image_path))

# l = detect_objects(local_image_path)
# print(l[0].object_property)

st.title("物体検出アプリ")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img)

uploaded_file = st.file_uploader("Choose Image to upload…", type=(["jpg", "jpeg"]))

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption="Uploaded image")
