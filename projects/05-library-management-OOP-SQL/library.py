from book import Book 
from validations import get_confirmation, user_input, get_int_value
from storage import connect_database

"""
Library Class

This module contains the Library class, which manages books
stored in a PostgreSQL database.

The Library class performs SQL operations, converts database
records into Book objects, and provides the application's
business logic.
"""


class Library:
    """
    Represents the library management system.

    Provides methods to add, search, borrow, return, delete
    and display books stored within the PostgreSQL database.
    """

    def __init__(self):
        """
        Initialise an empty library.
        
        Creates a list used to store Book objects.
        """

        self.books = []

    def add_book(self):
        """
        Add a new book to the library.

        ollects book details from the user, creates a Book object,
        checks for duplicate titles, and inserts the book into the
        PostgreSQL database if it does not already exist.
        """
        title = user_input("Enter Book Title (press X to cancel): ")
        if title is None:
            return  
        author = user_input("Enter Author (press X to cancel): ")
        if author is None:
            return
        genre = user_input("Enter Genre (press X to cancel): ")
        if genre is None:
            return
        year = get_int_value("Enter Year(press X to cancel): ")
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
                    
                cursor.close()
                connection.close()
                return

        else:
            cursor.execute("INSERT INTO books" \
            " (title, author, genre, year, available)" \
            " VALUES" \
            " (%s,%s,%s,%s,%s)",
                (book.title, book.author, book.genre, book.year, book.available))
    
            connection.commit()
            print("Book has been successfully added!")
    
            cursor.close()
            connection.close()
            return 
    
    def search_by_title(self):
        """
        Search for books by title.

        Retrieves books whose title matches the user's
        search and displays the matching results.
        """

        title = user_input("Enter Book Title (press X to cancel): ")
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
        """
        Search for books by author.

        Retrieves books written by the specified author
        and displays the matching results.
        """

        author = user_input("Enter Book Author (press X to cancel): ")
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
        """
        Search for books by genre.

        Retrieves books belonging to the specified genre
            and displays the matching results.
        """

        genre = user_input("Enter Book Genre (press X to cancel): ")
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
        """
        Display every book in the library.

        Retrieves all books from the PostgreSQL database,
        converts each database record into a Book object,
        and displays the book's information.
        """

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
        """
        Display all available books.

        Retrieves all books marked as available from the
        PostgreSQL database and displays their information.
        """

        connection, cursor = connect_database()

        cursor.execute("SELECT * FROM  books" \
        " WHERE available = True")

        books = cursor.fetchall()
        if not books:
            print("Currently No Books Avaiable")

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
        """
        Display all borrowed books.

        Retrieves all books currently marked as borrowed
        from the PostgreSQL database and displays them.
        """

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

    def borrow_book(self):
        """
        Borrow a book.

        Retrieves the selected book from the database,
        verifies that it is available, updates its
        availability status and saves the change.
        """

        title = user_input("Enter Book Title (press X to cancel): ")
        if title is None:
            return 

        author = user_input("Enter Book Author (press X to cancel): ")
        if author is None:
            return 

        connection,cursor = connect_database()

        cursor.execute("SELECT * FROM books" \
        " WHERE title ILIKE %s "
        " AND author ILIKE %s",
         (title, author))

        book = cursor.fetchone()
        if not book:
            print("Book does not exist!")

            cursor.close()
            connection.close()
            return 

        id, title, author, genre, year, available = book
        book = Book(title, author, genre, year, available)
        book.display_book()

        confirm = get_confirmation("Confirm book (Y/N): ")
        if not confirm:
            print("cancelling...")
            return 

        if not book.available:
            print("Book has already been borrowed")

            cursor.close()
            connection.close()
            return 

        cursor.execute("UPDATE books" \
        " SET available = False" \
        " WHERE title ILIKE %s " \
        " AND author ILIKE %s",
         (book.title, book.author))

        connection.commit()
        print("Book has been successfully borrowed!")

        cursor.close()
        connection.close()

    def return_book(self):
        """
        Return a borrowed book.

        Retrieves the selected book from the database,
        verifies that it is currently borrowed, updates
        its availability status and saves the change.
        """

        title = user_input("Enter Book Title (press X to cancel): ")
        if title is None:
            return 
        
        author = user_input("Enter Book Author (press X to cancel): ")
        if author is None:
            return 
        
        connection,cursor = connect_database()
        
        cursor.execute("SELECT * FROM books" \
        " WHERE title ILIKE %s "
        " AND author ILIKE %s",
         (title, author))
        
        book = cursor.fetchone()
        if not book:
            print("Book does not exist!")
        
            cursor.close()
            connection.close()
            return 
        
        id, title, author, genre, year, available = book
        book = Book(title, author, genre, year, available)
        book.display_book()

        confirm = get_confirmation("Confirm book (Y/N): ")
        if not confirm:
            print("cancelling...")
            return 

        
        if book.available:
            print("Book has already been returned")
        
            cursor.close()
            connection.close()
            return 
        
        cursor.execute("UPDATE books" \
        " SET available = True" \
        " WHERE title ILIKE %s " \
        " AND author ILIKE %s",
         (book.title, book.author))
        
        connection.commit()
        print("Book has been successfully returned!")
        
        cursor.close()
        connection.close()

    def delete_book(self):
        """
        Delete a book from the library.

        Retrieves the selected book from the database,
        confirms the deletion with the user, then removes
        the book from the PostgreSQL database.
        """

        title = user_input("Enter Book Title (press X to cancel): ")
        if title is None:
            return 
                
        author = user_input("Enter Book Author (press X to cancel): ")
        if author is None:
            return 
                
        connection,cursor = connect_database()
                
        cursor.execute("SELECT * FROM books" \
        " WHERE title ILIKE %s "
        " AND author ILIKE %s",
         (title, author))
                
        book = cursor.fetchone()
        if not book:
            print("Book does not exist!")
                
            cursor.close()
            connection.close()
            return 
                
        id, title, author, genre, year, available = book
        book = Book(title, author, genre, year, available)
        book.display_book()
        
        confirm = get_confirmation("Confirm book (Y/N): ")
        if not confirm:
            print("cancelling...")

            cursor.close()
            connection.close()
            return 
        
        cursor.execute("DELETE FROM books" \
        " WHERE title ILIKE %s" \
        " AND author ILIKE %s",
         (book.title, book.author))

        connection.commit()
        print("Book has been successfully deleted")

        cursor.close()
        connection.close()

    def overall_statistics(self):
        """
        Display overall library statistics.

        Retrieves summary information from the PostgreSQL
            database, including the total number of books,
        available books and borrowed books.
        """
        
        connection, cursor = connect_database()

        cursor.execute("SELECT COUNT(*) FROM books")

        result = cursor.fetchone()
        value= result[0]
        print(f"Total books: {value}")

        cursor.close()
        connection.close()

    def books_by_genre(self):
        """
        Display statistics by genre.

        Counts and displays the number of books belonging
        to each genre stored in the database.
        """

        connection, cursor = connect_database()

        cursor.execute("SELECT genre, COUNT(*)" \
        " FROM books" \
        " GROUP BY genre " \
        " ORDER BY genre")

        rows = cursor.fetchall()
        print("\n --- Books by Genre ---")
        for genre, count in rows:
            print(f"{genre}: {count}")

            cursor.close()
            connection.close()

    def books_by_author(self):
        """
        Display statistics by author.

        Counts and displays the number of books written
        by each author stored in the database.
        """

        connection, cursor = connect_database()
    
        cursor.execute("SELECT author, COUNT(*)" \
        " FROM books" \
        " GROUP BY author " \
        " ORDER BY author")
    
        rows = cursor.fetchall()
        print("\n --- Books by Authors ---")
        for author, count in rows:
            print(f"{author}: {count}")
    
            cursor.close()
            connection.close()
    








