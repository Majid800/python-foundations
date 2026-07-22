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
    
            connection, cursor = connect_database()

            cursor.execute("SELECT * FROM books" \
            " WHERE title ILIKE %s" \
            " AND author ILIKE %s",
            (book.title, book.author))
            existing_book = cursor.fetchone()
            if existing_book:
                    print("Book already exists!")
                    #
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
    
    def search_by_title(self):
        title = user_input("Enter Book Title  (press X to cancel): ")
        if title is None:
            return  

        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM books" \
        " WHERE title ILIKE %s", \
         (title,) )
        rows = cursor.fetchall()

        if not rows:
            print("Book does not exist!")

            cursor.close()
            connection.close()
            return

        print("\n --- Books ---")
        for id, title, author, genre, year, available in rows:
            book = Book(title, author, genre, year)
            book.display_book()

            cursor.close()
            connection.close()
            return 
             

    def search_by_author(self):
        author = user_input("Enter Book Author  (press X to cancel): ")
        if author is None:
            return  

        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM books" \
        " WHERE author ILIKE %s", \
         (author,) )
        rows = cursor.fetchall()

        if not rows:
            print("Book does not exist!")

            cursor.close()
            connection.close()
            return

        print(f"\n --- {author} ---")
        for id, title, author, genre, year, available in rows:
            book = Book(title, author, genre, year)
            book.display_book()

            cursor.close()
            connection.close()
            return 

    def search_by_genre(self):
        genre = user_input("Enter Book Genre  (press X to cancel): ")
        if genre is None:
            return  
        
        connection, cursor = connect_database()
        
        cursor.execute("SELECT * FROM books" \
        " WHERE genre ILIKE %s", \
         (genre,) )
        rows = cursor.fetchall()
        
        if not rows:
            print("Genre does not exist!")

            cursor.close()
            connection.close()
            return
        
        print(f"\n --- {genre} ---")
        for id, title, author, genre, year, available in rows:
            book = Book(title, author, genre, year)
            book.display_book()
        
            cursor.close()
            connection.close()
            return 


    def view_all_books(self):
        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM books")

        books = cursor.fetchall()
        if not books:
            print("There are no books to view")

            cursor.close()
            connection.close()
            return 

         
        print("\n --- All Books ---")
        for id, title, author, genre, year, available in books:
            book = Book(title, author, genre, year, available)
            book.display_book()

            cursor.close()
            connection.close()

    def view_available_books(self):

        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM  books" \
        " WHERE available = True")

        books = cursor.fetchall()
        if not books:
            print("No Available Books Currently")

            cursor.close()
            connection.close()
            return 

        print("\n --- Available Books ---")
        for id, title, author, genre, year, available in books:
            book = Book(title, author, genre, year, available)
            book.display_book()

            cursor.close()
            connection.close()

    def view_borrowed_books(self):

        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM books" \
        " WHERE available = False")

        books = cursor.fetchall()
        if not books:
            print("Currently No Books Borrowed")

            cursor.close()
            connection.close()
            return
            

        print("\n --- Borrowed Books ---")
        for id, title, author, genre, year, available in books:
            book = Book(title, author, genre, year, available)
            book.display_book()

