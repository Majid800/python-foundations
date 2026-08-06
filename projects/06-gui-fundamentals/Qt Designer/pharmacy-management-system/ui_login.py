
from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QWidget)
from resources import res_rc

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(814, 668)
        Form.setStyleSheet(u"QWidget#Form {\n"
"background: rgb(255, 233, 255);\n"
"}\n"
"\n"
"QPushButton#btn_login{\n"
"	color: rgb(0, 0, 0);\n"
"border: 2px solid black;\n"
"background-color: rgb(0, 170, 255);\n"
"}\n"
"\n"
"QPushButton#btn_login:hover {\n"
"text-decoration: underline;\n"
"color: rgb(0,0,180);\n"
"}\n"
"\n"
"\n"
"QPushButton#btn_forgtpwd{\n"
"background-color: transparent;\n"
"border:none;\n"
"color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#btn_forgtpwd:hover{\n"
"text-decoration: underline;\n"
"color: rgb(0,0,180);\n"
"}\n"
"\n"
"QPushButton#btn_create_new_user{\n"
"background-color: transparent;\n"
"border:none;\n"
"color: rgb(0, 0, 127);\n"
"}\n"
"\n"
"QPushButton#btn_create_new_user:hover{\n"
"text-decoration: underline;\n"
"color: rgb(0,0,180);\n"
"}\n"
"\n"
"QCheckBox#checkbox_remember{\n"
"color: rgb(0,0,127);\n"
"}\n"
"\n"
"QLabel#error_label1 {\n"
"color: rgb(255, 0, 0);}\n"
"\n"
"QLabel#error_label2 {\n"
"color: rgb(255, 0, 0);}\n"
"\n"
"QLabel#login_validation_label{\n"
"color: rgb(255, 0, 0);}\n"
"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(50, 130, 721, 421))
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 341, 421))
        self.label.setStyleSheet(u"background-image: url(:/images/pharmacy2.jpg);\n"
"border-top-left-radius: 50px;\n"
"")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(320, 0, 391, 421))
        font = QFont()
        font.setPointSize(10)
        self.label_3.setFont(font)
        self.label_3.setStyleSheet(u"background-color:rgba(255,255,255,255);\n"
"border-bottom-right-radius: 50px;")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(430, 30, 140, 100))
        font1 = QFont()
        font1.setFamilies([u"Microsoft Tai Le"])
        font1.setPointSize(20)
        font1.setBold(True)
        self.label_4.setFont(font1)
        self.label_4.setStyleSheet(u"color: rgba(0,0,0,200);")
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.txt_username = QLineEdit(self.widget)
        self.txt_username.setObjectName(u"txt_username")
        self.txt_username.setGeometry(QRect(390, 130, 220, 40))
        font2 = QFont()
        font2.setPointSize(13)
        self.txt_username.setFont(font2)
        self.txt_username.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 5px solid rgb(30,30,30);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;\n"
"}\n"
"")
        self.txt_username.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.txt_username_2 = QLineEdit(self.widget)
        self.txt_username_2.setObjectName(u"txt_username_2")
        self.txt_username_2.setGeometry(QRect(390, 220, 220, 40))
        self.txt_username_2.setFont(font2)
        self.txt_username_2.setStyleSheet(u"QLineEdit{\n"
"background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"border-bottom: 5px solid rgb(30,30,30);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;\n"
"}\n"
"")
        self.txt_username_2.setEchoMode(QLineEdit.EchoMode.Password)
        self.txt_username_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.btn_login = QPushButton(self.widget)
        self.btn_login.setObjectName(u"btn_login")
        self.btn_login.setGeometry(QRect(450, 320, 111, 31))
        font3 = QFont()
        font3.setFamilies([u"Microsoft Tai Le"])
        font3.setPointSize(14)
        font3.setBold(True)
        self.btn_login.setFont(font3)
        self.btn_forgtpwd = QPushButton(self.widget)
        self.btn_forgtpwd.setObjectName(u"btn_forgtpwd")
        self.btn_forgtpwd.setGeometry(QRect(550, 290, 131, 26))
        font4 = QFont()
        font4.setFamilies([u"Microsoft Tai Le"])
        font4.setPointSize(9)
        font4.setBold(True)
        self.btn_forgtpwd.setFont(font4)
        self.btn_create_new_user = QPushButton(self.widget)
        self.btn_create_new_user.setObjectName(u"btn_create_new_user")
        self.btn_create_new_user.setGeometry(QRect(360, 290, 131, 26))
        font5 = QFont()
        font5.setFamilies([u"Microsoft Tai Le"])
        font5.setBold(True)
        self.btn_create_new_user.setFont(font5)
        self.error_label2 = QLabel(self.widget)
        self.error_label2.setObjectName(u"error_label2")
        self.error_label2.setGeometry(QRect(390, 270, 221, 16))
        font6 = QFont()
        font6.setFamilies([u"Microsoft Tai Le"])
        font6.setPointSize(12)
        font6.setBold(True)
        self.error_label2.setFont(font6)
        self.error_label1 = QLabel(self.widget)
        self.error_label1.setObjectName(u"error_label1")
        self.error_label1.setGeometry(QRect(390, 190, 221, 16))
        self.error_label1.setFont(font6)
        self.login_validation_label = QLabel(self.widget)
        self.login_validation_label.setObjectName(u"login_validation_label")
        self.login_validation_label.setGeometry(QRect(400, 390, 211, 20))
        font7 = QFont()
        font7.setPointSize(15)
        self.login_validation_label.setFont(font7)
        self.login_validation_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label_2 = QLabel(Form)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(170, 40, 461, 71))
        font8 = QFont()
        font8.setFamilies([u"Microsoft Tai Le"])
        font8.setPointSize(22)
        font8.setBold(True)
        self.label_2.setFont(font8)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText("")
        self.label_3.setText("")
        self.label_4.setText(QCoreApplication.translate("Form", u"LOG IN", None))
        self.txt_username.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.txt_username_2.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.btn_login.setText(QCoreApplication.translate("Form", u"LOGIN", None))
        self.btn_forgtpwd.setText(QCoreApplication.translate("Form", u"forgotten password?", None))
        self.btn_create_new_user.setText(QCoreApplication.translate("Form", u"Create New User", None))
        self.error_label2.setText("")
        self.error_label1.setText("")
        self.login_validation_label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"Pharmacy Management System", None))
    # retranslateUi

