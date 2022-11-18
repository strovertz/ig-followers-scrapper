from asyncio.windows_events import NULL
from PIL import Image
from pytesseract import pytesseract
from selenium import webdriver 
from selenium.webdriver.chrome.options import Options
from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup


def catch_images():
    from urllib.request import urlopen
    from bs4 import BeautifulSoup
    html = urlopen("https://www.python.org/")
    res = BeautifulSoup(html.read(),"html5lib");
    print(res.title)
 
def get_path():
    #Define path to tessaract.exe
    path_to_tesseract = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

    profiles = ['images/teste.png', 'images/sampletext1-ocr.png']

    lista = []
    #catch_images()
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

        return lista

def words():
    search_this = ["Analista", "Sistemas", "UFSM"]
    return search_this

def result(n):
    result = ["Estudante da UFSM", "Nao Estudante"]
    return result[n]
