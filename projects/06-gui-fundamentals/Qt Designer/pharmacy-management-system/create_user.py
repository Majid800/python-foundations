from PySide6.QtWidgets import QWidget
from ui_create_user import Ui_Form


class CreateUserWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.setup_window()
        self.connect_signals()


    def setup_window(self):
        self.ui.password_requirements_widget.hide()


    def connect_signals(self):
        self.ui.email_entry.editingFinished.connect(self.email_validation)
        self.ui.email_entry.textEdited.connect(self.clear_email_error)
        self.ui.firstname_entry.editingFinished.connect(self.first_name_validation)
        self.ui.firstname_entry.textEdited.connect(self.clear_firstname_error)
        self.ui.lastname_entry.editingFinished.connect(self.last_name_validation)
        self.ui.lastname_entry.textEdited.connect(self.clear_lastname_error)
        self.ui.username_entry.editingFinished.connect(self.username_validation)
        self.ui.username_entry.textEdited.connect(self.clear_username_error)
        self.ui.password_entry.textEdited.connect(self.live_password_validation)
        self.ui.password_entry.editingFinished.connect(self.password_validation)
        self.ui.retype_password_entry.editingFinished.connect(self.retype_password_valdation)
        self.ui.retype_password_entry.textEdited.connect(self.clear_retype_password_error)




    def email_validation(self):
        email = self.ui.email_entry.text()

        if not email:
            self.ui.email_error_label.setText("Email Required")
            return False

        if email.count("@") != 1:
            self.ui.email_error_label.setText("Enter Valid Email Format")
            return False 

        username, domain = email.split("@")
        if not username:
            self.ui.email_error_label.setText("Enter Valid Email Format")
            return False 

        if not domain:
            self.ui.email_error_label.setText("Enter Valid Email Format")
            return False 

        self.ui.email_error_label.clear()
        return True 

    def clear_email_error(self):
        self.ui.email_error_label.clear()

    def first_name_validation(self):
        first_name = self.ui.firstname_entry.text()

        if not first_name:
            self.ui.firstname_error_label.setText("First Name Required")
            return False 

        if not first_name.isalpha():
            self.ui.firstname_error_label.setText("Name Cannot Contain Numbers")
            return False 

        self.ui.firstname_error_label.clear()
        return True 

    def clear_firstname_error(self):
        self.ui.firstname_error_label.clear()

    def last_name_validation(self):
            last_name = self.ui.lastname_entry.text()
    
            if not last_name:
                self.ui.lastname_error_label.setText("Last Name Required")
                return False 
    
            if not last_name.isalpha():
                self.ui.lastname_error_label.setText("Name Cannot Contain Numbers")
                return False 
    
            self.ui.lastname_error_label.clear()
            return True 
    
    def clear_lastname_error(self):
        self.ui.lastname_error_label.clear()

    def username_validation(self):
        username = self.ui.username_entry.text()

        if not username:
            self.ui.username_error_label.setText("Username Required")
            return False 

        found = False 
        for character in username:
            if character.isalpha():
                found = True 
                break 

        if not found:
            self.ui.username_error_label.setText("Username Must Contain A Number")
            return False 

        self.ui.username()

    def clear_username_error(self):
        self.ui.username_error_label.clear()

    def password_validation(self):
        password = self.ui.password_entry.text()

        if not password:
            self.ui.password_error_label.setText("Password Required")
            return False


        self.ui.password_error_label.clear()
        return True

    def live_password_validation(self):
        self.ui.password_requirements_widget.show()

        password = self.ui.password_entry.text()

        if not password:
            return

    # Starts with uppercase
        if password[0].isupper():
            self.ui.label_2.setText("✓ Starts with Uppercase")
        else:
            self.ui.label_2.setText("✗ Starts with Uppercase")

    # Minimum 8 characters
        if len(password) >= 8:
            self.ui.label_3.setText("✓ Minimum 8 characters")
        else:
            self.ui.label_3.setText("✗ Minimum 8 characters")

    # At least one symbol
        found_symbol = False
        for character in password:
            if not character.isalpha() and not character.isdigit():
                found_symbol = True
                break

        if found_symbol:
            self.ui.label_4.setText("✓ At least one symbol")
        else:
            self.ui.label_4.setText("✗ At least one symbol")

    def clear_password_error(self):
        self.ui.password_error_label.clear()

    def retype_password_valdation(self):
        retype_password = self.ui.retype_password_entry.text()
        password = self.ui.password_entry.text()

        if password == retype_password:
            self.ui.retype_password_error_label.setText("Passwords do not match")
            return False

        self.ui.retype_password_error_label.clear()
        return True 

    def clear_retype_password_error(self):
        self.ui.retype_password_entry.clear()
