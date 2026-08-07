from database import get_books, get_books_by_genre, get_available_books, get_books_by_keyword
from PySide6.QtWidgets import QTableWidgetItem
from ui_sidebar import Ui_MainWindow

class BookManager:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui 

        self.connect_signals()
        self.populate_table()


    def connect_signals(self):
        # Category Combo Box 
        self.ui.category_combo.currentTextChanged.connect(self.select_genre_combobox)
        
            # Genre Combo Box for searching books
        self.ui.genre_combo.currentTextChanged.connect(self.search_by_genre)
        
            # Available Combo Box for Searching Books
        self.ui.available_combo.currentTextChanged.connect(self.search_by_availability)
        
            # Live Search 
        self.ui.books_search.textChanged.connect(self.search_by_keyword)

    def display_books(self, books):
            for row, book in enumerate(books):
                for column, value in enumerate(book):
                    if column == 5:
                        if value:
                            value = "Available"
                        else:
                            value = "Borrowed"
                    self.ui.books_table_widget.setItem(
                        row,
                        column,
                        QTableWidgetItem(str(value))
                        )



    def populate_table(self):
            books = get_books()
    
            self.ui.books_table_widget.setRowCount(len(books))
    
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
        self.ui.books_table_widget.setRowCount(0)
        self.ui.books_table_widget.setRowCount(len(books))
    
        self.display_books(books)
    
    def search_by_availability(self):
        status = self.ui.available_combo.currentText()
        if status == "Available":
            available = True
        elif status == "Borrowed":
            available = False
    
        books = get_available_books(available)
        self.ui.books_table_widget.setRowCount(0)
        self.ui.books_table_widget.setRowCount(len(books))
    
        self.display_books(books)
    
    def search_by_keyword(self):
        keyword = self.ui.books_search.text()
    
        books = get_books_by_keyword(keyword)
        self.ui.books_table_widget.setRowCount(0)
        self.ui.books_table_widget.setRowCount(len(books))
        self.display_books(books)
    
        
