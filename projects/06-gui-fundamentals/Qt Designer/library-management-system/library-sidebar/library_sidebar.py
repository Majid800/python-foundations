import sys 

from ui_sidebar import Ui_MainWindow
from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QTableWidgetItem
from database import get_books, get_books_by_genre, get_available_books

class MySideBar(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.icons_names_widget.hide()

        self.connect_signals()
        self.populate_table()

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

    # Category Combo Box 
        self.ui.category_combo.currentTextChanged.connect(self.select_genre_combobox)

    # Genre Combo Box for searching books
        self.ui.genre_combo.currentTextChanged.connect(self.search_by_genre)

    # Available Combo Box for Searching Books
        self.ui.available_combo.currentTextChanged.connect(self.search_by_availability)


    # Helper Functions
    def display_books(self, books):
         for row, book in enumerate(books):
            for column, value in enumerate(book):
                if column == 5:
                    if value:
                        value = "Available"
                    else:
                        value = "Borrowed"
                self.ui.tableWidget.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                        )


    ## Books Page ## 

    # Populate Table with Data
    
    def populate_table(self):
        books = get_books()

        self.ui.tableWidget.setRowCount(len(books))

        self.display_books(books)



    def select_genre_combobox(self):
        
        category = self.ui.category_combo.currentText()

        if category == "Fiction":
            self.ui.genre_combo.clear()
            self.ui.genre_combo.addItems([
                "Fantasy",
                "Thriller",
                "Sci-fi",
                "Mystery",
                "Romance",
                "Dystopian",
                "Classic",
                "Horror",
                "Dark Fantasy",  
            ])

        elif category == "Non-Fiction":
            self.ui.genre_combo.clear()
            self.ui.genre_combo.addItems([
                "Biography",
                "Autobiography",
                "Maths",
                "Science",
                "Economics",
                "True Crime",
                "Politics",
                "Popular Science",
                "Nature",
                "Travel Writing",
                "Food Writing",
                "Philosophy",
                "Religion"
            ])

    def search_by_genre(self):
        genre = self.ui.genre_combo.currentText()

        
        books = get_books_by_genre(genre)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(books))

        self.display_books(books)

    def search_by_availability(self):
        status = self.ui.available_combo.currentText()
        if status == "Available":
            available = True
        elif status == "Borrowed":
            available = False

        books = get_available_books(available)
        self.ui.tableWidget.setRowCount(0)
        self.ui.tableWidget.setRowCount(len(books))

        self.display_books(books)

        