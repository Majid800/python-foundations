import sys 
from books import BookManager
from ui_sidebar import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem
from borrow_return import BorrowReturnManager
from home_dashboard import HomeDashboardManager

class MySideBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icons_names_widget.hide()

        
        self.connect_signals()
        self.books = BookManager(self.ui)
        self.borrow_return = BorrowReturnManager(self.ui)
        self.dashboard = HomeDashboardManager(self.ui)

    def connect_signals(self):
            # Dashboard
        self.ui.dashboard_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))
        self.ui.dashboard_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(0))

    # Books
        self.ui.books_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1))
        self.ui.books_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(1)
    )

    # Borrow / Return
        self.ui.return_borrow_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))
        self.ui.return_borrow_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(2))

    # Statistics
        self.ui.stats_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))
        self.ui.stats_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(3))

    # Settings
        self.ui.settings_1.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))
        self.ui.settings_2.clicked.connect(lambda: self.ui.stackedWidget.setCurrentIndex(4))

  




        