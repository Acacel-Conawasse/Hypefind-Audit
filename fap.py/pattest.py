import pyautogui
import pytesseract
from PIL import Image
import time
    
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

extracted_text = pytesseract.image_to_string("C:/Users/omalomo3/Desktop/Hypefind Audit/fap.py/image.png")

print (extracted_text)