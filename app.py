# import PIL as Image
# 直接importしてあげる
import PIL.Image as Image
import PIL.ImageDraw as ImageDraw
import PIL.ImageFont as ImageFont
import streamlit as st

from detect_tags import detect_objects, get_tags

# local_image_path = "/Users/a81701/code/streamlit/detection/02_物体検出アプリ/sample01.jpg"
# # print(get_tags(local_image_path))

# l = detect_objects(local_image_path)
# print(l[0].object_property)

st.title("物体検出アプリ")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    image_path = f"img/{uploaded_file.name}"
    img.save(image_path)

    draw = ImageDraw.Draw(img)
    objects = detect_objects(image_path)
    for obj in objects:
        x = obj.rectangle.x
        y = obj.rectangle.y
        w = obj.rectangle.w
        h = obj.rectangle.h
        caption = obj.object_property

        font = ImageFont.truetype(font="./Helvetica 400.ttf", size=40)
        text_w, text_h = draw.textsize(caption, font=font)
        draw.rectangle([(x, y), (x + w, y + h)], fill=None, outline="green", width=5)
        draw.rectangle([(x, y), (x + text_w, y + text_h)], fill="green")
        draw.text((x, y), caption, fill="white", font=font)
    st.image(img)

    tags_name = get_tags(image_path)
    print(tags_name)
    # みやすいようにカンマ区切りに整形
    tags_name = ", ".join(tags_name)
    st.markdown("**識別されたタグ**")
    st.markdown(f">{tags_name}")
