import base64
import os
import streamlit as st
import reveal_slides as rs


# Чтение markdown слайдов
with open("presentation.md", "r", encoding="utf-8") as f:
    slides_content = f.read()

def image_to_base64(path):
    with open(path, "rb") as img_file:
        return base64.b64encode(img_file.read()).decode()

    # 1. Конвертируем все изображения сразу


img1_base64 = image_to_base64("optimized.jpg")
img2_base64 = image_to_base64("photo_2.png")
img3_base64 = image_to_base64("photo_3.png")
img4_base64 = image_to_base64("photo_4.png")
img5_base64 = image_to_base64("photo_5.png")
img6_base64 = image_to_base64("photo_6.png")
img7_base64 = image_to_base64("photo_7.png")
img8_base64 = image_to_base64("photo_8.png")
img9_base64 = image_to_base64("photo_9.png")
img10_base64 = image_to_base64("photo_10.png")
img11_base64 = image_to_base64("photo_11.png")
img12_base64 = image_to_base64("photo_12.png")
img13_base64 = image_to_base64("photo_13.png")
img14_base64 = image_to_base64("photo_14.png")
img15_base64 = image_to_base64("photo_15.png")
img16_base64 = image_to_base64("photo_16.png")
img17_base64 = image_to_base64("photo_17.png")

# 2. Создаем HTML-теги
img_html = f'<img src="data:image/jpeg;base64,{img1_base64}" style="width:70%;">'
img2_html = f'<img src="data:image/png;base64,{img2_base64}" style="width:70%;">'
img3_html = f'<img src="data:image/png;base64,{img3_base64}" style="width:70%;">'
img4_html = f'<img src="data:image/png;base64,{img4_base64}" style="width:70%;">'
img5_html = f'<img src="data:image/png;base64,{img5_base64}" style="width:70%;">'
img6_html = f'<img src="data:image/png;base64,{img6_base64}" style="width:70%;">'
img7_html = f'<img src="data:image/png;base64,{img7_base64}" style="width:70%;">'
img8_html = f'<img src="data:image/png;base64,{img8_base64}" style="width:70%;">'
img9_html = f'<img src="data:image/png;base64,{img9_base64}" style="width:70%;">'
img10_html = f'<img src="data:image/png;base64,{img10_base64}" style="width:70%;">'
img11_html = f'<img src="data:image/png;base64,{img11_base64}" style="width:70%;">'
img12_html = f'<img src="data:image/png;base64,{img12_base64}" style="width:70%;">'
img13_html = f'<img src="data:image/png;base64,{img13_base64}" style="width:70%;">'
img14_html = f'<img src="data:image/png;base64,{img14_base64}" style="width:70%;">'
img15_html = f'<img src="data:image/png;base64,{img15_base64}" style="width:70%;">'
img16_html = f'<img src="data:image/png;base64,{img16_base64}" style="width:70%;">'
img17_html = f'<img src="data:image/png;base64,{img17_base64}" style="width:70%;">'


# 3. Однократное чтение файла и замена

replacements = {
    "{img_html}": img_html,
    "{img_2}": img2_html,
    "{img_3}": img3_html,
    "{img_4}": img4_html,
    "{img_5}": img5_html,
    "{img_6}": img6_html,
    "{img_7}": img7_html,
    "{img_8}": img8_html,
    "{img_9}": img9_html,
    "{img_10}": img10_html,
    "{img_11}": img11_html,
    "{img_12}": img12_html,
    "{img_13}": img13_html,
"{img_14}": img14_html,
"{img_15}": img15_html,
"{img_16}": img16_html,
"{img_17}": img17_html,


}

with open("presentation.md", "r", encoding="utf-8") as f:
    md_content = f.read()
    for placeholder, html in replacements.items():
        md_content = md_content.replace(placeholder, html)

rs.slides(content=md_content,
          theme="serif",
          config={
              "plugins": ["highlight"],
              "pluginsConfig": {
                  "highlight": {
                      "theme": "monokai"
                  }
              }
          }
          )










# with open("presentation.md", "r", encoding="utf-8") as f:
#     md_content = f.read() \
#         .replace("{img_html}", img_html) \
#         .replace("{img_2}", img2_html) \
#         .replace("{img_3}", img3_html) \
#         .replace("{img_4}", img4_html) \
#         .replace("{img_5}", img5_html) \
#         .replace("{img_6}", img6_html) \
#         .replace("{img_7}", img7_html) \
#         .replace("{img_8}", img8_html)
#
#             rs.slides(content=md_content, theme="serif")




