from PySide6.QtGui import QFont

# FONTS and STYLES

# Window
window_style = """
            background-color: #00ff80;
            """



# Heading 
heading_font = QFont("Arial", 30, QFont.Bold)
heading_style = """
            background-color: #00ff80;
            color: #ffffff;   """

# Labels
label_font = QFont("calibri", 16)
label_style =  """
                background-color: #00ff80;
                color: #000000;
                """

# Options Font 
options_font = QFont("calibri", 12, QFont.Bold)

# Remember me Checkbox 
remember_me_style = """
            background-color: #00ff80;
            color: #000000;
            """

# Mouse Hover Style 
mouse_hover_style =  """
            QPushButton {
            border: none;
            background-color: transparent;
            color: #0000a0;
            text-decoration: none;
            }
            QPushButton:hover {
            text-decoration: underline}
            """

# Error Label 
error_label_font = QFont("calibri", 16, QFont.Bold)
error_style = """
            background-color: #00ff80;
            color: #ff0000;
            """

#  Role Radio Buttons 
radio_button_font = QFont("calibri", 14)
radio_button_style = label_style

# Permissions Checkboxes
permissions_checkboxes_font = QFont("calibri", 14)
permissions_checkboxes_style = label_style


# Button 
button_font = QFont("calibri", 20, QFont.Bold)
button_style = """
            background-color: #00ff80;
            color:#000000;
            """










