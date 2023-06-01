import cv2
import mss
import numpy
import pytesseract
import pyautogui
from time import sleep

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def main():
    global mon
    sleep(3)
    with mss.mss() as sct:
        while True:
            im = numpy.asarray(sct.grab(mon))

            text = pytesseract.image_to_string(im)
            text = text.replace("\n", " ")

            pyautogui.typewrite(text + " ", 0.01)
            mon = {'top': 415, 'left': 375, 'width': 1200, 'height': 110}

input("Press Enter to start")
mon = {'top': 360, 'left': 375, 'width': 1200, 'height': 110}
main()