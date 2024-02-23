import mss
import numpy
import pytesseract
import pyautogui
from time import sleep
from keyboard import is_pressed

pytesseract.pytesseract.tesseract_cmd = 'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def main():
    global mon
    global left
    global top
    sleep(3)
    with mss.mss() as sct:
        while True:
            im = numpy.asarray(sct.grab(mon))

            text = pytesseract.image_to_string(im)
            text = text.replace("\n", " ")

            pyautogui.typewrite(text + " ", 0.01)
            top1 = top + 95
            mon = {'top': top1, 'left': left, 'width': 1200, 'height': 110}
            if is_pressed('q'):
                idk = 0
                print("Bye.")
                print(len(idk))

input("Press Enter to start")
left = pyautogui.locateOnScreen('eng.png', confidence=0.8, grayscale=True)[0]
top = pyautogui.locateOnScreen('eng.png', confidence=0.8, grayscale=True)[1]
left -= 535
top1 = top + 40
mon = {'top': top1, 'left': left, 'width': 1200, 'height': 110}
main()