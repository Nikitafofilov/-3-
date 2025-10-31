
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGroupBox, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(567, 211)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setGeometry(QRect(170, 5, 391, 161))
        self.labelImgCAPTCHA = QLabel(self.groupBox)
        self.labelImgCAPTCHA.setObjectName(u"labelImgCAPTCHA")
        self.labelImgCAPTCHA.setGeometry(QRect(10, 20, 371, 131))
        self.labelImgCAPTCHA.setPixmap(QPixmap(u"6bxwg.png"))
        self.labelImgCAPTCHA.setScaledContents(True)
        self.groupBox_2 = QGroupBox(self.centralwidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setGeometry(QRect(10, 10, 161, 156))
        self.pushButtonDecryptImg = QPushButton(self.groupBox_2)
        self.pushButtonDecryptImg.setObjectName(u"pushButtonDecryptImg")
        self.pushButtonDecryptImg.setGeometry(QRect(5, 80, 151, 51))
        self.pushButtonDecryptImg.setAutoDefault(False)
        self.pushButtonGenImg = QPushButton(self.groupBox_2)
        self.pushButtonGenImg.setObjectName(u"pushButtonGenImg")
        self.pushButtonGenImg.setGeometry(QRect(5, 10, 151, 51))
        self.pushButtonGenImg.setAutoDefault(False)
        self.labelSymbols = QLabel(self.centralwidget)
        self.labelSymbols.setObjectName(u"labelSymbols")
        self.labelSymbols.setGeometry(QRect(11, 171, 151, 26))
        self.labelSymbols.setLayoutDirection(Qt.LeftToRight)
        self.labelSymbols.setTextFormat(Qt.AutoText)
        self.textEditCAPTHA = QTextEdit(self.centralwidget)
        self.textEditCAPTHA.setObjectName(u"textEditCAPTHA")
        self.textEditCAPTHA.setGeometry(QRect(150, 170, 411, 31))
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u0412\u0437\u043b\u043e\u043c \u043a\u0430\u043f\u0447\u0438", None))
        self.groupBox.setTitle(QCoreApplication.translate("MainWindow", u"\u0418\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435 \u043a\u0430\u043f\u0447\u0438", None))
        self.labelImgCAPTCHA.setText("")
        self.groupBox_2.setTitle("")
        self.pushButtonDecryptImg.setText(QCoreApplication.translate("MainWindow", u"\u0420\u0430\u0441\u0448\u0438\u0444\u0440\u043e\u0432\u0430\u0442\u044c \u043a\u0430\u043f\u0447\u0443", None))
        self.pushButtonGenImg.setText(QCoreApplication.translate("MainWindow", u"\u041e\u0431\u043d\u043e\u0432\u0438\u0442\u044c \u0438\u0437\u043e\u0431\u0440\u0430\u0436\u0435\u043d\u0438\u0435", None))
        self.labelSymbols.setText(QCoreApplication.translate("MainWindow", u"\u041f\u043e\u0441\u043b\u0435\u0434\u043e\u0432\u0430\u0442\u0435\u043b\u044c\u043d\u043e\u0441\u0442\u044c \n"
"\u0441\u0438\u043c\u0432\u043e\u043b\u043e\u0432:", None))
    # retranslateUi

