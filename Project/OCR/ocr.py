from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os

# Path to the PDF file
pdf_path = r"C:\Users\gopir\Downloads\New doc 23-May-2021 11.28 am.pdf"

# Path to the Poppler executable if not in system PATH (for Windows)
poppler_path = r"E:\jupiter"

# Convert PDF to a list of images
images = convert_from_path(pdf_path, poppler_path=poppler_path if os.name == 'nt' else None)
print(type(images),images,sep="\n")
# Loop through each image and extract text
for i, image in enumerate(images):
    # Optionally, save the image for debugging purposes
    image_path = f'page_{i+1}.png'
    image.save(image_path, 'PNG')
    
    # Extract text from the image
    text = pytesseract.image_to_string(image)
    
    print(f"Text from page {i+1}:")
    print(text)
    print("-" * 50)
