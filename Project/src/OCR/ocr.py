import pytesseract
from PIL import Image
import fitz
from io import BytesIO
from pytesseract import Output

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
        with Image.open(image_path) as image: # Need to check this line
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
        pdf_document = fitz.open(image)

        for page_number in range(len(pdf_document)):
            page = pdf_document.load_page(page_number)
            pix = page.get_pixmap()
            # Load the image from bytes into a PIL Image object
            img = Image.open(BytesIO(pix.tobytes()))
            text = pytesseract.image_to_string(img)
        return text #-----------------------------------------> need to change the logic of return
    except Exception as e:
        return f"An error occurred: {e}"

def image_to_data(img, lang='eng'):
    """
    Extracts text and data from an image using Tesseract OCR.
    Parameters:
    - img (PIL.PngImagePlugin.PngImageFile): The path to the image file.
    - lang (str): The language to use for OCR (default is 'eng' for English).
    Returns:
    - dict: A dictionary containing extracted text and data.
    """

    # Use pytesseract to extract text and data
    text = pytesseract.image_to_data(img, lang=lang, output_type=Output.DICT)
    return text

  
    
print(image_to_text_tess(r"C:\Users\harih\OneDrive\Desktop\ocr_nlp\ocr_nlp_project\Project\Data\Images\photo_34_2024-01-17_12-42-32.jpg"))
