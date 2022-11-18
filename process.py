from asyncio.windows_events import NULL
from PIL import Image
from pytesseract import pytesseract

#Define path to tessaract.exe
path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

profiles = ['images/teste.png', 'images/sampletext1-ocr.png']

lista = []

#Define path to image
for i in profiles:
    path_to_image = i

    #Point tessaract_cmd to tessaract.exe
    pytesseract.tesseract_cmd = path_to_tesseract

    #Open image with PIL
    img = Image.open(path_to_image)

    #Extract text from image
    text = pytesseract.image_to_string(img)

    lista.append(text)
