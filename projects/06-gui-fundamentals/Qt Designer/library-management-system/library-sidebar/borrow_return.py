from PySide6.QtWidgets import QTableWidgetItem, QMessageBox
from database import get_books, get_books_by_genre, get_available_books, get_books_by_keyword, book_borrowed, book_returned
from ui_sidebar import Ui_MainWindow


class BorrowReturnManager:
    def __init__(self, ui):
        self.ui: Ui_MainWindow = ui
        
        
        self.connect_signals()
        self.populate_table()
        self.ui.selected_book_frame.hide()


    def connect_signals(self):
        # Search Bar 
        self.ui.borrow_return_search.textChanged.connect(self.search_books)

        # Selecting book from Table 
        self.ui.borrow_return_table_widget.itemClicked.connect(self.select_book)

        # Borrow Book
        self.ui.borrow_button.clicked.connect(self.borrow_book)

        # Return Book
        self.ui.return_button.clicked.connect(self.return_book)


    def display_books(self, books):
        for row, book in enumerate(books):
            for column, value in enumerate(book):
                if column == 5:
                    if value:
                        value = "Available"
                    else:
                        value = "Borrowed"
                self.ui.borrow_return_table_widget.setItem(
                    row,
                    column,
                    QTableWidgetItem(str(value))
                        )
    
    def populate_table(self):
        books = get_books()
        self.ui.borrow_return_table_widget.setRowCount(len(books))
        self.display_books(books)
            
    def search_books(self):
        keyword = self.ui.borrow_return_search.text()
            
        books = get_books_by_keyword(keyword)
        self.ui.borrow_return_table_widget.setRowCount(0)
        self.ui.borrow_return_table_widget.setRowCount(len(books))
        self.display_books(books)





    def select_book(self, item):
        # Item clicked by user generates the row. From row we can store the columns inside that row as variables.
        row = item.row()

        book_id = self.ui.borrow_return_table_widget.item(row, 0).text()
        title = self.ui.borrow_return_table_widget.item(row, 1).text()
        author = self.ui.borrow_return_table_widget.item(row, 2).text()
        genre = self.ui.borrow_return_table_widget.item(row, 3).text()
        year = self.ui.borrow_return_table_widget.item(row, 4).text()
        status = self.ui.borrow_return_table_widget.item(row, 5).text()

        self.ui.selected_id_label.setText(book_id)
        self.ui.selected_title_label.setText(title)
        self.ui.selected_author_label.setText(author)
        self.ui.selected_genre_label.setText(genre)
        self.ui.selected_year_label.setText(year)
        self.ui.selected_status_label.setText(status)

        self.selected_book_id = int(book_id)

        self.ui.selected_book_frame.show()

    def borrow_book(self):
        book_id = self.selected_book_id

        result = book_borrowed(book_id)
        if result:
            QMessageBox.information(
                None, 
                "Success",
                "You have Successfully borrowed the book"
            )
        else:
            QMessageBox.warning(
                None,
                "Borrow Failed",
                "This book has already been borrowed"
            )

    def return_book(self):
        book_id = self.selected_book_id
        
        result = book_returned(book_id)
        if result:
            QMessageBox.information(
                None, 
                "Success",
                "You have Successfully returned the book"
                )
        else:
            QMessageBox.warning(
                None,
                "Return Failed",
                "This book has already been returned"
                    )
        






