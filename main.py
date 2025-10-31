import sys
import os
import random
import cv2
import pytesseract


pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
from PIL import Image
import numpy as np

from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import (QApplication,QMainWindow, QTableWidgetItem,QListWidgetItem, QComboBox, QTableWidget)

from ui_main import Ui_MainWindow

pathImgs= "./img"

custom_config = r'''
--oem 3            # OCR Engine Mode: LSTM только
--psm 6           # Page Segmentation Mode: один символ (если капча посимвольно)
--dpi 300         # Указываем DPI для корректного масштабирования
--tessedit_char_whitelist=0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz
'''
class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        self.ui.pushButtonDecryptImg.setEnabled(False)
        self.pathImgCaptcha = ""

        self.ui.pushButtonGenImg.clicked.connect(self.displayCaptcha)
        self.ui.pushButtonDecryptImg.clicked.connect(self.solveCaptcha)


    # Отображает случайную капчу из каталога. Программа также запоминает имя капчи, которая изображена в пользовательском интерфейсе.
    def displayCaptcha (self):
        files = [f for f in os.listdir(pathImgs)
                    if os.path.isfile(os.path.join(pathImgs, f))]
        self.pathImgCaptcha = pathImgs+"/"+random.choice(files)
        pixmapCaptcha = QPixmap(self.pathImgCaptcha)
        self.ui.labelImgCAPTCHA.setPixmap(pixmapCaptcha)
        self.ui.pushButtonDecryptImg.setEnabled(True)

    def solveCaptcha(self):
       image=cv2.resize((cv2.imread(self.pathImgCaptcha)),(400,80))
       grayImage = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
       ret, binaryImage = cv2.threshold(grayImage, 254, 255, cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
       blurred = cv2.medianBlur(binaryImage, 3)
       kernel = np.ones((2, 2), np.uint8)
       erode = cv2.erode(blurred,kernel,iterations = 1)
       opening = cv2.morphologyEx(erode, cv2.MORPH_OPEN, kernel,iterations=1)

       contours, _ = cv2.findContours(opening, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)


       result = opening.copy()


       min_area = 20

       filtered_contours = []
       for contour in contours:
           area = cv2.contourArea(contour)

           if area >= min_area:

               filtered_contours.append(contour)
           else:
               cv2.drawContours(result, [contour], -1, 0, -1)
       self.ui.textEditCAPTHA.setText(pytesseract.image_to_string(Image.fromarray(result),config=custom_config))

if __name__ == "__main__":
    app = QApplication.instance()
    if not app:
        app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())
