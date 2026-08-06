# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'pharmacy-create-user.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QRadioButton, QSizePolicy, QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(1280, 675)
        Form.setStyleSheet(u"QWidget#Form {\n"
"background: rgb(255, 233, 255);\n"
"}\n"
"\n"
"QWidget{ \n"
"background: rgb(255, 215, 250);\n"
"border-radius: 20px;\n"
"}\n"
"\n"
"QWidget#form_widget{\n"
"background: rgb(255, 195, 255);\n"
"}\n"
"\n"
"QWidget#roles_widget{\n"
"background: rgb(255, 195, 255);\n"
"}\n"
"QWidget#permissions_widget{\n"
"background: rgb(255, 195, 255);\n"
"}\n"
"\n"
"\n"
"QLabel{\n"
"background: rgb(255, 195, 255);\n"
"}\n"
"\n"
"QLabel#heading_label{\n"
"background: rgb(255, 215, 250);\n"
"color:rgba(57, 57, 57, 178)\n"
"}\n"
"\n"
"QLineEdit{\n"
"background-color: rgb(255, 195, 255);\n"
"border: none;\n"
"border-bottom: 5px solid rgb(30,30,30);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;\n"
"}\n"
"\n"
"QRadioButton{\n"
"background: rgb(255, 195, 255);\n"
"}\n"
"QCheckBox{\n"
"background: rgb(255, 195, 255);\n"
"}\n"
"QPushButton{\n"
"background-color: rgb(255, 166, 220);\n"
"border: 2px solid rgb(30,30,30);\n"
"color: rgba(0,0,0,240);\n"
"padding-bottom: 7px;\n"
"}\n"
"")
        self.widget = QWidget(Form)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(-60, 0, 1311, 661))
        self.heading_label = QLabel(self.widget)
        self.heading_label.setObjectName(u"heading_label")
        self.heading_label.setGeometry(QRect(550, 10, 281, 31))
        font = QFont()
        font.setFamilies([u"Microsoft Tai Le"])
        font.setPointSize(24)
        font.setBold(True)
        self.heading_label.setFont(font)
        self.heading_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.form_widget = QWidget(self.widget)
        self.form_widget.setObjectName(u"form_widget")
        self.form_widget.setGeometry(QRect(450, 40, 481, 421))
        font1 = QFont()
        font1.setFamilies([u"Segoe UI Semibold"])
        self.form_widget.setFont(font1)
        self.password_entry = QLineEdit(self.form_widget)
        self.password_entry.setObjectName(u"password_entry")
        self.password_entry.setGeometry(QRect(260, 260, 150, 30))
        font2 = QFont()
        font2.setFamilies([u"Microsoft Tai Le"])
        font2.setPointSize(12)
        self.password_entry.setFont(font2)
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.lastname_entry = QLineEdit(self.form_widget)
        self.lastname_entry.setObjectName(u"lastname_entry")
        self.lastname_entry.setGeometry(QRect(260, 140, 150, 30))
        self.lastname_entry.setFont(font2)
        self.retype_password_entry = QLineEdit(self.form_widget)
        self.retype_password_entry.setObjectName(u"retype_password_entry")
        self.retype_password_entry.setGeometry(QRect(260, 310, 150, 30))
        self.retype_password_entry.setFont(font2)
        self.retype_password_entry.setEchoMode(QLineEdit.EchoMode.Password)
        self.email_label = QLabel(self.form_widget)
        self.email_label.setObjectName(u"email_label")
        self.email_label.setGeometry(QRect(100, 30, 150, 20))
        font3 = QFont()
        font3.setFamilies([u"Microsoft Tai Le"])
        font3.setPointSize(12)
        font3.setBold(True)
        self.email_label.setFont(font3)
        self.email_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.password_label = QLabel(self.form_widget)
        self.password_label.setObjectName(u"password_label")
        self.password_label.setGeometry(QRect(100, 260, 150, 20))
        self.password_label.setFont(font3)
        self.username_entry = QLineEdit(self.form_widget)
        self.username_entry.setObjectName(u"username_entry")
        self.username_entry.setGeometry(QRect(260, 200, 150, 30))
        self.username_entry.setFont(font2)
        self.username_label = QLabel(self.form_widget)
        self.username_label.setObjectName(u"username_label")
        self.username_label.setGeometry(QRect(100, 200, 150, 20))
        self.username_label.setFont(font3)
        self.lastname_label = QLabel(self.form_widget)
        self.lastname_label.setObjectName(u"lastname_label")
        self.lastname_label.setGeometry(QRect(100, 140, 150, 20))
        self.lastname_label.setFont(font3)
        self.firstname_label = QLabel(self.form_widget)
        self.firstname_label.setObjectName(u"firstname_label")
        self.firstname_label.setGeometry(QRect(100, 80, 150, 20))
        self.firstname_label.setFont(font3)
        self.firstname_entry = QLineEdit(self.form_widget)
        self.firstname_entry.setObjectName(u"firstname_entry")
        self.firstname_entry.setGeometry(QRect(260, 80, 150, 30))
        self.firstname_entry.setFont(font2)
        self.email_entry = QLineEdit(self.form_widget)
        self.email_entry.setObjectName(u"email_entry")
        self.email_entry.setGeometry(QRect(260, 30, 150, 30))
        self.email_entry.setFont(font2)
        self.retype_password_label = QLabel(self.form_widget)
        self.retype_password_label.setObjectName(u"retype_password_label")
        self.retype_password_label.setGeometry(QRect(100, 310, 150, 20))
        self.retype_password_label.setFont(font3)
        self.email_error_label = QLabel(self.form_widget)
        self.email_error_label.setObjectName(u"email_error_label")
        self.email_error_label.setGeometry(QRect(260, 60, 151, 20))
        font4 = QFont()
        font4.setPointSize(8)
        self.email_error_label.setFont(font4)
        self.firstname_error_label = QLabel(self.form_widget)
        self.firstname_error_label.setObjectName(u"firstname_error_label")
        self.firstname_error_label.setGeometry(QRect(260, 110, 151, 20))
        self.firstname_error_label.setFont(font4)
        self.lastname_error_label = QLabel(self.form_widget)
        self.lastname_error_label.setObjectName(u"lastname_error_label")
        self.lastname_error_label.setGeometry(QRect(260, 170, 151, 20))
        self.lastname_error_label.setFont(font4)
        self.username_error_label = QLabel(self.form_widget)
        self.username_error_label.setObjectName(u"username_error_label")
        self.username_error_label.setGeometry(QRect(260, 230, 151, 20))
        self.username_error_label.setFont(font4)
        self.password_error_label = QLabel(self.form_widget)
        self.password_error_label.setObjectName(u"password_error_label")
        self.password_error_label.setGeometry(QRect(260, 290, 151, 20))
        self.password_error_label.setFont(font4)
        self.retype_password_error_label = QLabel(self.form_widget)
        self.retype_password_error_label.setObjectName(u"retype_password_error_label")
        self.retype_password_error_label.setGeometry(QRect(260, 340, 151, 20))
        self.retype_password_error_label.setFont(font4)
        self.password_requirements_widget = QWidget(self.form_widget)
        self.password_requirements_widget.setObjectName(u"password_requirements_widget")
        self.password_requirements_widget.setGeometry(QRect(50, 330, 201, 80))
        self.password_requirements_widget.setStyleSheet(u"background: rgb(220, 34, 180);\n"
"\n"
"QLabel{\n"
"	color: rgb(0, 0, 0);\n"
"	font-family: \"Gabriola\";\n"
"	font-szie: 11pt;\n"
"	font-weight: bold;\n"
"}")
        self.label_2 = QLabel(self.password_requirements_widget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 20, 161, 16))
        font5 = QFont()
        font5.setFamilies([u"Gabriola"])
        font5.setPointSize(11)
        self.label_2.setFont(font5)
        self.label_3 = QLabel(self.password_requirements_widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 60, 161, 16))
        self.label_3.setFont(font5)
        self.label_4 = QLabel(self.password_requirements_widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 40, 161, 16))
        self.label_4.setFont(font5)
        self.label = QLabel(self.password_requirements_widget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 0, 171, 20))
        font6 = QFont()
        font6.setFamilies([u"Gabriola"])
        font6.setPointSize(14)
        font6.setBold(True)
        self.label.setFont(font6)
        self.label.setStyleSheet(u"QLabel{color: blue:}")
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.roles_widget = QWidget(self.widget)
        self.roles_widget.setObjectName(u"roles_widget")
        self.roles_widget.setGeometry(QRect(450, 460, 211, 161))
        self.role_label = QLabel(self.roles_widget)
        self.role_label.setObjectName(u"role_label")
        self.role_label.setGeometry(QRect(20, 10, 81, 16))
        self.role_label.setFont(font3)
        self.role_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.pharmacist_radiobutton = QRadioButton(self.roles_widget)
        self.pharmacist_radiobutton.setObjectName(u"pharmacist_radiobutton")
        self.pharmacist_radiobutton.setGeometry(QRect(20, 30, 98, 24))
        font7 = QFont()
        font7.setFamilies([u"Microsoft Tai Le"])
        self.pharmacist_radiobutton.setFont(font7)
        self.dispenser_radiobutton = QRadioButton(self.roles_widget)
        self.dispenser_radiobutton.setObjectName(u"dispenser_radiobutton")
        self.dispenser_radiobutton.setGeometry(QRect(20, 60, 98, 24))
        self.dispenser_radiobutton.setFont(font7)
        self.technician_radiobutton = QRadioButton(self.roles_widget)
        self.technician_radiobutton.setObjectName(u"technician_radiobutton")
        self.technician_radiobutton.setGeometry(QRect(20, 90, 98, 24))
        self.technician_radiobutton.setFont(font7)
        self.permissions_widget = QWidget(self.widget)
        self.permissions_widget.setObjectName(u"permissions_widget")
        self.permissions_widget.setGeometry(QRect(720, 460, 211, 161))
        self.permissions_label = QLabel(self.permissions_widget)
        self.permissions_label.setObjectName(u"permissions_label")
        self.permissions_label.setGeometry(QRect(20, 10, 101, 16))
        self.permissions_label.setFont(font3)
        self.permissions_label.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)
        self.dispense_checkbox = QCheckBox(self.permissions_widget)
        self.dispense_checkbox.setObjectName(u"dispense_checkbox")
        self.dispense_checkbox.setGeometry(QRect(20, 30, 171, 24))
        self.check_prescriptions_checkbox = QCheckBox(self.permissions_widget)
        self.check_prescriptions_checkbox.setObjectName(u"check_prescriptions_checkbox")
        self.check_prescriptions_checkbox.setGeometry(QRect(20, 60, 171, 24))
        self.pmr_checkbox = QCheckBox(self.permissions_widget)
        self.pmr_checkbox.setObjectName(u"pmr_checkbox")
        self.pmr_checkbox.setGeometry(QRect(20, 120, 171, 24))
        self.order_checkbox = QCheckBox(self.permissions_widget)
        self.order_checkbox.setObjectName(u"order_checkbox")
        self.order_checkbox.setGeometry(QRect(20, 90, 171, 24))
        self.createuser_button = QPushButton(self.widget)
        self.createuser_button.setObjectName(u"createuser_button")
        self.createuser_button.setGeometry(QRect(470, 620, 161, 41))
        font8 = QFont()
        font8.setFamilies([u"Microsoft Tai Le"])
        font8.setPointSize(15)
        font8.setBold(True)
        self.createuser_button.setFont(font8)
        self.clear_button = QPushButton(self.widget)
        self.clear_button.setObjectName(u"clear_button")
        self.clear_button.setGeometry(QRect(750, 620, 161, 41))
        self.clear_button.setFont(font8)
        self.clear_button.setFlat(False)
        self.submit_label = QLabel(self.widget)
        self.submit_label.setObjectName(u"submit_label")
        self.submit_label.setGeometry(QRect(170, 180, 201, 161))
        font9 = QFont()
        font9.setPointSize(17)
        self.submit_label.setFont(font9)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.heading_label.setText(QCoreApplication.translate("Form", u"Create New User", None))
        self.password_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Password", None))
        self.lastname_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Last Name", None))
        self.retype_password_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Retype password", None))
        self.email_label.setText(QCoreApplication.translate("Form", u"Email: ", None))
        self.password_label.setText(QCoreApplication.translate("Form", u"Password", None))
        self.username_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Username", None))
        self.username_label.setText(QCoreApplication.translate("Form", u"Username:", None))
        self.lastname_label.setText(QCoreApplication.translate("Form", u"Last Name: ", None))
        self.firstname_label.setText(QCoreApplication.translate("Form", u"First Name:", None))
        self.firstname_entry.setPlaceholderText(QCoreApplication.translate("Form", u"First Name", None))
        self.email_entry.setPlaceholderText(QCoreApplication.translate("Form", u"Email", None))
        self.retype_password_label.setText(QCoreApplication.translate("Form", u"Retype Password", None))
        self.email_error_label.setText("")
        self.firstname_error_label.setText("")
        self.lastname_error_label.setText("")
        self.username_error_label.setText("")
        self.password_error_label.setText("")
        self.retype_password_error_label.setText("")
        self.label_2.setText(QCoreApplication.translate("Form", u"\u2718 Start with Uppercase", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u2718Atleast one symbol", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u2718Minimum 8 characters", None))
        self.label.setText(QCoreApplication.translate("Form", u"Password Requirements", None))
        self.role_label.setText(QCoreApplication.translate("Form", u"Role", None))
        self.pharmacist_radiobutton.setText(QCoreApplication.translate("Form", u"Pharmacist", None))
        self.dispenser_radiobutton.setText(QCoreApplication.translate("Form", u"Dispenser", None))
        self.technician_radiobutton.setText(QCoreApplication.translate("Form", u"Technician", None))
        self.permissions_label.setText(QCoreApplication.translate("Form", u"Permissions", None))
        self.dispense_checkbox.setText(QCoreApplication.translate("Form", u"Dispense prescriptions", None))
        self.check_prescriptions_checkbox.setText(QCoreApplication.translate("Form", u"Check Prescriptions", None))
        self.pmr_checkbox.setText(QCoreApplication.translate("Form", u"Access PMRs", None))
        self.order_checkbox.setText(QCoreApplication.translate("Form", u"Order Stock", None))
        self.createuser_button.setText(QCoreApplication.translate("Form", u"CREATE USER", None))
        self.clear_button.setText(QCoreApplication.translate("Form", u"CLEAR", None))
        self.submit_label.setText("")
    # retranslateUi

