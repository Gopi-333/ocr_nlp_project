from ocr import image_to_text_tess, image_to_data
import cv2
import matplotlib.pyplot as plt
from PIL import Image
import pytesseract
import io 

img = cv2.imread(r"C:\Users\harih\OneDrive\Desktop\ocr_nlp\ocr_nlp_project\Project\Data\sample insurence img\1.png")
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

# pil_image = Image.fromarray(otsu_threshold_img)
# Normal Image
pil_image = Image.fromarray(img)
image_bytes = io.BytesIO()
pil_image.save(image_bytes, format='PNG')
image_bytes.seek(0)


# Gray Scale image
pil_gray_image = Image.fromarray(gray_scale_image)
gray_image_bytes = io.BytesIO()
pil_gray_image .save(gray_image_bytes, format='PNG')
gray_image_bytes.seek(0)


# Threshold image
pil_thres_image = Image.fromarray(gray_scale_image)
thres_image_bytes = io.BytesIO()
pil_thres_image.save(thres_image_bytes, format='PNG')
thres_image_bytes.seek(0)


print("********************")
print("Check 1: Original")
print("********************")
# print(image_to_data(img))
print(image_to_text_tess(image_bytes))


print("-----------------------------")
print("Check 2: Gray scale only")
print("-----------------------------")
# print(image_to_data(gray_scale_image))
print(image_to_text_tess(gray_image_bytes))

print("+++++++++++++++++++++++++++++++++")
print("Threshold image")
print("+++++++++++++++++++++++++++++++++")
# print(image_to_data(otsu_threshold_img)) 
print(image_to_text_tess(thres_image_bytes))

# output_path = r"C:\Users\harih\Downloads\gray_scale_image.jpg"
# cv2.imwrite(output_path, gray_scale_image)