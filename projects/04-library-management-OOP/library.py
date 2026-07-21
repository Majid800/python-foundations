#creates library class that has the list of books inside and performs functions to the books
from book import Book
from validations import user_input, get_int_value, get_confirmation

class library:
    def __init__(self):
        self.books = []

    def add_book(self):
        title = user_input("Please enter Title: (press X to cancel): ")
        if title is None:
            return
        author = user_input("Please enter Author: (press X to cancel): ")
        if author is None:
            return 
        genre = user_input("Please enter genre: (press X to cancel): ")
        if genre is None:
            return
        year = get_int_value("Please enter year: (press X to cancel): ")
        if year is None:
            return
        available = True
        
        book = Book(title, author, genre, year, available)
        book.display_book()
        confirm = get_confirmation("Confirm this book (Y/N): ")
        if not confirm:
            print("Cancelling...")
            return 
        
        for existing_book in self.books:
            if book.title == existing_book.title and author.title == existing_book.author:
                print("Book already exists!")
                return 
            
        self.books.append(book)
        print("Book added successfully!")
        

    
    

