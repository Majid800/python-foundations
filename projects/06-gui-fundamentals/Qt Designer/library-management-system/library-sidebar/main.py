from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton
import sys
from library_sidebar import MySideBar

if __name__ == "__main__":

    app = QApplication(sys.argv)

    window = MySideBar()
    window.show()

    app.exec()
