import pytesseract
from PIL import Image

def extract_text_from_image(image_path, lang='eng'):
    """
    Extracts text from an image using Tesseract OCR.

    Parameters:
    - image_path (str): The path to the image file.
    - lang (str): The language to use for OCR (default is 'eng' for English).

    Returns:
    - str: The text extracted from the image.
    """
    try:
        # Open the image file
        with Image.open(image_path) as image:
            # Use pytesseract to extract text
            text = pytesseract.image_to_string(image, lang=lang)
        return text
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
# text = extract_text_from_image('path_to_image.jpg')
# print(text)
