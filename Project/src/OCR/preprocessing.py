from ocr import image_to_text_tess, image_to_data
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
import io 

img = cv2.imread(r"C:\Users\harih\Downloads\New doc 23-May-2021 11.28 am_page-0001.jpg")
gray_scale_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
# adaptive_gaussian_threshold_img = cv2.adaptiveThreshold(gray_scale_image, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 9)
value, otsu_threshold_img = cv2.threshold(gray_scale_image,0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU )
# adaptive_threshold_img = cv2.adaptiveThreshold(gray_scale_image,255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 11, 9 )
# print(img.shape)
# print(adaptive_gaussian_threshold_img.shape)
# plt.imshow(img)
# plt.axis("off")
# plt.show()
# plt.imshow(adaptive_gaussian_threshold_img, cmap='gray')
plt.imshow(otsu_threshold_img, cmap="gray")
# plt.imshow(adaptive_threshold_img, cmap="gray")
plt.axis("off")
plt.show()

pil_image = Image.fromarray(otsu_threshold_img)

image_bytes = io.BytesIO()
pil_image.save(image_bytes, format='PNG')
image_bytes.seek(0)

print(image_to_data(gray_scale_image))

# output_path = r"C:\Users\harih\Downloads\gray_scale_image.jpg"
# cv2.imwrite(output_path, gray_scale_image)