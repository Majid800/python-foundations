import sys 
from PySide6.QtWidgets import ( QApplication, QWidget, QLabel, QPushButton, 
                               QMainWindow, QLineEdit, QVBoxLayout, QHBoxLayout, QCheckBox, QDialog, QRadioButton)
from PySide6.QtGui import QFont
from PySide6.QtCore import Qt
from styles import (
    label_font, label_style , heading_font, heading_style, remember_me_style, mouse_hover_style,
    error_label_font, error_style, window_style, options_font, button_font, button_style, radio_button_font, radio_button_style,
    permissions_checkboxes_font, permissions_checkboxes_style
)

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.create_window()
        self.create_widgets()
        self.style_widgets()
        self.create_layout()
        self.connect_signals()



    def create_window(self):
        self.setWindowTitle("practice")
        self.resize(400,300)
        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        # Login Panel
        self.login_panel = QWidget()
       

    # Creates the layout after creating the central widget of QMainWindow. Horizontal or vertical layout. Once the layout has beencreated the central widget is set with the layout
    # Created and then inside create_layout you add the widgets you created inside that layout. The job is not to create widgets but to arrange widgets 
    
    def create_widgets(self):

        # Title Label
        self.title_label = QLabel("💊 Pharmacy Management System 💊")

        # Username Label and Entry
        self.username_label = QLabel("Username:")
        self.username_entry = QLineEdit()

        # Username Error Label
        self.username_error_label = QLabel()

        # Password Label and Entry
        self.password_label = QLabel("password:")
        self.password_entry = QLineEdit()
        self.password_entry.setEchoMode(QLineEdit.EchoMode.Password)

        # Password Error Label
        self.password_error_label = QLabel()


        
        # Remember me checkbox label
        self.remember_me_checkbox = QCheckBox("Remember Me")

        # Forgotten password Button
        self.forgotten_password_label = QPushButton("Forgotten Password?")

        

        # Login Button
        self.login_button = QPushButton("Login")

        # Create User
        self.create_user_label = QPushButton("Create User")

    def style_widgets(self):
        # Window Style
        self.setStyleSheet(window_style)

        # Heading 
        self.title_label.setFont(heading_font)
        self.title_label.setStyleSheet(heading_style)

        # Labels 
        self.username_label.setFont(label_font)
        self.username_label.setStyleSheet(label_style)

        self.password_label.setFont(label_font)
        self.password_label.setStyleSheet(label_style)

        # Entry widths
        self.username_entry.setFixedWidth(250)
        self.password_entry.setFixedWidth(250)

        # Remember Me Checbox 
        self.remember_me_checkbox.setFont(label_font)
        self.remember_me_checkbox.setStyleSheet(remember_me_style)

        # Create User
        self.create_user_label.setFont(label_font)
        self.create_user_label.setStyleSheet(mouse_hover_style)

        # Forgotten Password
        self.forgotten_password_label.setFont(label_font)
        self.forgotten_password_label.setStyleSheet(mouse_hover_style)

        # Error Labels
        self.username_error_label.setFont(error_label_font)
        self.username_error_label.setStyleSheet(error_style)

        self.password_error_label.setFont(error_label_font)
        self.password_error_label.setStyleSheet(error_style)

        # Login Button
        self.login_button.setFont(button_font)
        self.login_button.setStyleSheet(button_style)







    def create_layout(self):

        # Main Layout
        self.main_layout = QVBoxLayout()
        self.central_widget.setLayout(self.main_layout)
        

        # Login Panel Layout 
        self.panel_layout = QVBoxLayout()
        self.login_panel.setLayout(self.panel_layout)

        # Username Row 
        self.username_layout = QHBoxLayout()

        self.username_layout.addStretch()
        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_entry)
        self.username_layout.addStretch()
      

        # Password Row 
        self.password_layout = QHBoxLayout()

        self.password_layout.addStretch()
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_entry)
        self.password_layout.addStretch()
        

        # Options Row
        self.options_layout = QHBoxLayout()

        self.options_layout.addStretch()
        self.options_layout.addWidget(self.remember_me_checkbox)
        self.options_layout.addWidget(self.forgotten_password_label)
        self.options_layout.addStretch()


        # Build Login Panel
        self.panel_layout.addWidget(self.title_label, 
                                    alignment = Qt.AlignmentFlag.AlignCenter)
        self.panel_layout.addLayout(self.username_layout)
        self.panel_layout.addWidget(self.username_error_label, alignment = Qt.AlignmentFlag.AlignCenter)
        self.panel_layout.addLayout(self.password_layout)
        self.panel_layout.addWidget(self.password_error_label,
                                     alignment = Qt.AlignmentFlag.AlignCenter)
        self.panel_layout.addLayout(self.options_layout)
        self.panel_layout.addWidget(self.login_button, alignment = Qt.AlignmentFlag.AlignCenter)
        self.panel_layout.addWidget(self.create_user_label, alignment = Qt.AlignmentFlag.AlignCenter)


        
        self.main_layout.addStretch()

        self.main_layout.addWidget(self.login_panel,
                                                   alignment = Qt.AlignmentFlag.AlignCenter)

        self.main_layout.addStretch()

    

    
    def connect_signals(self):
        self.username_entry.editingFinished.connect(self.validate_username)
        self.username_entry.textChanged.connect(self.clear_username_error)
        self.password_entry.editingFinished.connect(self.validate_password)
        self.password_entry.textChanged.connect(self.clear_password_error)
        self.create_user_label.clicked.connect(self.open_create_user_dialog)
        

    #Connection Functions 
    def validate_username(self):
        username = self.username_entry.text()

        if not username:
            self.username_error_label.setText("Username is Required")
            
        else:
            self.username_error_label.clear()

    def clear_username_error(self):
        self.username_error_label.clear()

    def validate_password(self):
        password = self.password_entry.text()

        if not password:
            self.password_error_label.setText("Password is Required")

        else:
            self.password_error_label.clear()
       

    def clear_password_error(self):
        self.password_error_label.clear()

    # Create User Window function 
    def open_create_user_dialog(self):
        self.create_user_dialog = CreateUserDialog()
        self.create_user_dialog.exec()


# Create QDialog, which is a special type of window for temporary interactions
class CreateUserDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.create_user_window()
        self.create_user_widgets()
        self.style_widgets()
        self.create_layout()

    
    def create_user_window(self):
        self.setWindowTitle("Create User")
        self.resize(800,600)
        self.setStyleSheet(window_style)

        # Create User Panel
        self.create_user_panel = QWidget()


    def create_user_widgets(self):
        self.create_user_label = QLabel("Create a User")

        self.email_label = QLabel("Email: ")
        self.email_label_entry = QLineEdit()

        self.first_name_label = QLabel("First Name: ")
        self.first_name_entry = QLineEdit()

        self.last_name_label = QLabel("Last Name: ")
        self.last_name_entry = QLineEdit()

        self.username_label = QLabel("First Name: ")
        self.username_entry = QLineEdit()

        self.password_label = QLabel("Password: ")
        self.password_entry = QLineEdit()

        self.retype_password_label = QLabel("Retype Password: ")
        self.retype_password_entry = QLineEdit()

        self.roles_label = QLabel("Select a Role")
        self.pharmacist_option = QRadioButton("Pharmacist")
        self.dispenser_option = QRadioButton("Dispenser")
        self.technician_option = QRadioButton("technician")

        self.permissions_label = QLabel("Permissions")
        self.dispense_prescriptions_checkbox = QCheckBox("Dispense Prescriptions")
        self.check_prescriptions_checkbox = QCheckBox("Check Prescriptions")
        self.order_stock_checkbox = QCheckBox("Order Stock")
        self.access_pmr_checkbox = QCheckBox("Access PMR")

        self.create_button = QPushButton("Create") 
        self.clear_button = QPushButton("Clear")


    

    def style_widgets(self):
        # Heading 
        self.create_user_label.setFont(heading_font)
        self.create_user_label.setStyleSheet(heading_style)

        # Email 
        self.email_label.setFont(label_font)
        self.email_label.setStyleSheet(label_style)
        self.email_label.setFixedWidth(150)

        self.email_label_entry.setFixedWidth(250)

        # First Name
        self.first_name_label.setFont(label_font)
        self.first_name_label.setStyleSheet(label_style)
        self.first_name_label.setFixedWidth(150)

        self.first_name_entry.setFixedWidth(250)

        # Last Name
        self.last_name_label.setFont(label_font)
        self.last_name_label.setStyleSheet(label_style)
        self.last_name_label.setFixedWidth(150)

        self.last_name_entry.setFixedWidth(250)

        # Username
        self.username_label.setFont(label_font)
        self.username_label.setStyleSheet(label_style)
        self.username_label.setFixedWidth(150)

        self.username_entry.setFixedWidth(250)

        # Password 
        self.password_label.setFont(label_font)
        self.password_label.setStyleSheet(label_style)
        self.password_label.setFixedWidth(150)

        self.password_entry.setFixedWidth(250)

        # Retype Password 
        self.retype_password_label.setFont(label_font)
        self.retype_password_label.setStyleSheet(label_style)
        self.retype_password_label.setFixedWidth(150)

        self.retype_password_entry.setFixedWidth(250)

        # Roles
        self.roles_label.setFont(label_font)
        self.roles_label.setStyleSheet(label_style)

        self.pharmacist_option.setFont(radio_button_font)
        self.pharmacist_option.setStyleSheet(radio_button_style)

        self.dispenser_option.setFont(radio_button_font)
        self.dispenser_option.setStyleSheet(radio_button_style)

        self.technician_option.setFont(radio_button_font)
        self.technician_option.setStyleSheet(radio_button_style)

        #Permissions 
        self.permissions_label.setFont(label_font)
        self.permissions_label.setStyleSheet(label_style)

        self.dispense_prescriptions_checkbox.setFont(permissions_checkboxes_font)
        self.dispense_prescriptions_checkbox.setStyleSheet(permissions_checkboxes_style)

        self.check_prescriptions_checkbox.setFont(permissions_checkboxes_font)
        self.check_prescriptions_checkbox.setStyleSheet(permissions_checkboxes_style)

        self.order_stock_checkbox.setFont(permissions_checkboxes_font)
        self.order_stock_checkbox.setStyleSheet(permissions_checkboxes_style)

        self.access_pmr_checkbox.setFont(permissions_checkboxes_font)
        self.access_pmr_checkbox.setStyleSheet(permissions_checkboxes_style)

        # Buttons
        self.create_button.setFont(button_font)
        self.create_button.setStyleSheet(button_style)

        self.clear_button.setFont(button_font)
        self.clear_button.setStyleSheet(button_style)
    

    def create_layout(self):
        self.main_layout = QVBoxLayout()
        self.setLayout(self.main_layout)

        # Create User panel
        self.user_panel_widget = QWidget()

        self.user_panel_layout = QVBoxLayout()
        self.user_panel_widget.setLayout(self.user_panel_layout)


        # Email Row 
        self.email_layout = QHBoxLayout()

        self.email_layout.addStretch()
        self.email_layout.addWidget(self.email_label)
        self.email_layout.addWidget(self.email_label_entry)
        self.email_layout.addStretch()

        # First Name Row
        
        self.first_name_layout = QHBoxLayout()

        self.first_name_layout.addStretch()
        self.first_name_layout.addWidget(self.first_name_label)
        self.first_name_layout.addWidget(self.first_name_entry)
        self.first_name_layout.addStretch()

        # Last Name Row 
        self.last_name_layout = QHBoxLayout()

        self.last_name_layout.addStretch()
        self.last_name_layout.addWidget(self.last_name_label)
        self.last_name_layout.addWidget(self.last_name_entry)
        self.last_name_layout.addStretch()

        # Username Row 
        self.username_layout = QHBoxLayout()

        self.username_layout.addStretch()
        self.username_layout.addWidget(self.username_label)
        self.username_layout.addWidget(self.username_entry)
        self.username_layout.addStretch()

        # Password Row
        self.password_layout = QHBoxLayout()

        self.password_layout.addStretch()
        self.password_layout.addWidget(self.password_label)
        self.password_layout.addWidget(self.password_entry)
        self.password_layout.addStretch()

        # Retype Password Row
        self.retype_password_layout = QHBoxLayout()

        self.retype_password_layout.addStretch()
        self.retype_password_layout.addWidget(self.retype_password_label)
        self.retype_password_layout.addWidget(self.retype_password_entry)
        self.retype_password_layout.addStretch()

        # Roles and Permissions layout
        
        self.roles_permissions_widget = QWidget()
        self.roles_permissions_layout = QHBoxLayout()
        self.roles_permissions_widget.setLayout(self.roles_permissions_layout)



        # Roles Vertical Layout 
        self.roles_layout = QVBoxLayout()


        self.roles_layout.addWidget(self.roles_label)
        self.roles_layout.addWidget(self.pharmacist_option)
        self.roles_layout.addWidget(self.dispenser_option)
        self.roles_layout.addWidget(self.technician_option)

        # Permissions Vertical Layout 
        self.permissions_layout = QVBoxLayout()

        self.permissions_layout.addWidget(self.permissions_label)
        self.permissions_layout.addWidget(self.dispense_prescriptions_checkbox)
        self.permissions_layout.addWidget(self.check_prescriptions_checkbox)
        self.permissions_layout.addWidget(self.order_stock_checkbox)
        self.permissions_layout.addWidget(self.access_pmr_checkbox)

        self.roles_permissions_layout.addLayout(self.roles_layout)
        self.roles_permissions_layout.addLayout(self.permissions_layout)


        # Buttons 
        self.buttons_layout = QHBoxLayout()

        self.buttons_layout.addStretch()
        self.buttons_layout.addWidget(self.create_button)
        self.buttons_layout.addWidget(self.clear_button)
        self.buttons_layout.addStretch()

        # Add the widgets and layout to create user panel 

        self.user_panel_layout.addWidget(self.create_user_label, alignment= Qt.AlignmentFlag.AlignCenter)
        self.user_panel_layout.addLayout(self.email_layout)
        self.user_panel_layout.addLayout(self.first_name_layout)
        self.user_panel_layout.addLayout(self.last_name_layout)
        self.user_panel_layout.addLayout(self.username_layout)
        self.user_panel_layout.addLayout(self.password_layout)
        self.user_panel_layout.addLayout(self.retype_password_layout)
        self.user_panel_layout.addWidget(self.roles_permissions_widget)
        self.user_panel_layout.addLayout(self.buttons_layout)

        self.user_panel_layout.setSpacing(15)

        
        self.main_layout.addStretch()
        self.main_layout.addWidget(self.user_panel_widget, alignment= Qt.AlignmentFlag.AlignCenter)
        self.main_layout.addStretch()



    #def validation_required(self, entry, error_label, field_name):
        #text = entry.text().strip()

        #if not text:
            #error_label.setText(f"{field_name} is required")
            #return False

        #error_label.clear()


app = QApplication([])
window = MainWindow()
window.show()
app.exec()
        

