from book import Book 
from validations import get_confirmation, user_input, get_int_value
from storage import connect_database





class Library:
    def __init__(self):
        self.books = []

    def add_book(self):
            title = user_input("Enter Book Title  (press X to cancel): ")
            if title is None:
                return  
            author = user_input("Enter Author  (press X to cancel): ")
            if author is None:
                return
            genre = user_input("Enter Genre  (press X to cancel): ")
            if genre is None:
                return
            year = get_int_value("Enter Year (press X to cancel): ")
            if year is None:
                return 
        
            book = Book(title, author, genre, year)
            book.display_book()
            confirm = get_confirmation("Confirm this book (Y/N): ")
            if not confirm: 
                print("Cancelling... ")
                return 
    
            connection = connect_database()
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM books" \
            " WHERE title ILIKE %s" \
            " AND author ILIKE %s",
            (book.title, book.author))
            existing_book = cursor.fetchone()
            if existing_book:
                    print("Book already exists!")
                    cursor.close()
                    connection.close()
                    return
            else:
                cursor.execute("INSERT INTO books" \
                " (title, author, genre, year, available)" \
                " VALUES" \
                " (%s,%s,%s,%s,%s)",
                 (book.title, book.author, book.genre, book.year, book.available))
    
                cursor.commit()
                print("Book has been successfully added!")
    
                cursor.close()
                connection.close()
                return 
    

