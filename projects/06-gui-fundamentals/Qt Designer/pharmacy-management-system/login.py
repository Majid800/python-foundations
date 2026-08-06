from ui_login import Ui_Form
from PySide6.QtWidgets import (QApplication, QCheckBox, QLabel, QLineEdit,
    QPushButton, QWidget)
from database import connect_database, check_login
from create_user import CreateUserWindow

class LoginWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.connect_signals()


    def connect_signals(self):
        self.ui.txt_username.editingFinished.connect(self.validate_username)
        self.ui.txt_username.textChanged.connect(self.clear_username_error)
        self.ui.txt_username_2.editingFinished.connect(self.validate_password)
        self.ui.txt_username_2.textChanged.connect(self.clear_password_error)
        self.ui.btn_login.clicked.connect(self.submit_login)
        self.ui.btn_create_new_user.clicked.connect(self.open_create_user)


    def validate_username(self):
        username = self.ui.txt_username.text()

        if not username:
            self.ui.error_label1.setText("Username Required")
            return False

        self.ui.error_label1.clear()
        return True

    def clear_username_error(self):
        self.ui.error_label1.clear()
        return True 

    def validate_password(self):
        password = self.ui.txt_username_2.text()

        if not password:
            self.ui.error_label2.setText("Password Required")
            return False
        
        self.ui.error_label2.clear()
        return True

    def clear_password_error(self):
        self.ui.error_label2.clear()
        return True

    def submit_login(self):
        username_valid = self.validate_username()
        password_valid = self.validate_password()

        if not username_valid or not password_valid:
            return

        username = self.ui.txt_username.text()
        password = self.ui.txt_username_2.text() 

        result = check_login(username, password)
        if result == "user_not_found":
            self.ui.login_validation_label.setText("User Not Found")

        elif result == "incorrect_password":
            self.ui.login_validation_label.setText("Incorrect Password")

        elif result == "user_found":
            self.ui.login_validation_label.setStyleSheet("color: green;")
            self.ui.login_validation_label.setText("Welcome")
        
    def open_create_user(self):
        self.create_user_window = CreateUserWindow()
        self.create_user_window.show()
    




