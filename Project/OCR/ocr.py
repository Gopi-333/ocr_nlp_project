import pytesseract
from PIL import Image

def image_to_text_tess(image_path, lang='eng'):
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

def pdf_to_text_tess(image, lang='eng'):
    """
    Extracts text from an image using Tesseract OCR.

    Parameters:
    - image (PIL.PngImagePlugin.PngImageFile): The path to the image file.
    - lang (str): The language to use for OCR (default is 'eng' for English).

    Returns:
    - str: The text extracted from the image.
    """
    try:
            # Use pytesseract to extract text
        text = pytesseract.image_to_string(image, lang=lang)
        return text
    except Exception as e:
        return f"An error occurred: {e}"

# Example usage:
text = image_to_text_tess(r'E:\Python projects\OCR_NLP\ocr_nlp_project\Project\Data\Images\photo_4_2024-01-17_12-42-32.jpg')
print(text)
