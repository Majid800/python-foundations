#Library 
from validations import get_int_value, user_input, get_confirmation, get_menu_choice
from storage import connect_database

"""
Library Management Module

Contains the core library management functions including adding,
viewing, searching, borrowing, returning, and deleting books.

The library dictionary is passed as a parameter to each function
rather than being imported directly. This separates the application's
business logic from its data storage, allowing the same functions to
work with data loaded from JSON and making the code easier to maintain
and extend.
"""
def display_book(title,author,genre, year, available):
    """
    Displays the details of the specified book.

    Searches the library for the given book title, displays its
    details if found, and returns the book's information.
    Returns None if the book does not exist.
    """
    print(f"\nTitle: {title}")
    print(f"Author: {author}")
    print(f"Genre: {genre}")
    print(f"Year: {year}")
    status = "Available" if available else "Borrowed"
    print(f"status: {status}")


def search_menu():
    """
    Displays the search menu.

    Allows the user to choose whether to search
    books by title, author, or genre.
    """
    print("\n --- Search Book ---")
    print("1.Search by Title")
    print("2.Search by Author")
    print("3.Search by Genre")
    print("4.exit")

def search_by_title():
    title = user_input("Enter Book Title (press x to cancel): ")
    if title is None:
        return
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("" \
    "SELECT * FROM books WHERE title ILIKE %s",
    (title,))
    book = cursor.fetchone()
    if book is None:
        print("Book Not Found")
    else:
        id, title, author, genre, year, available = book
        display_book(title,author,genre,year,available)


    cursor.close()
    connection.close()

def search_by_author():
    author = user_input("Enter author name (press x to cancel): ")
    if author is None:
        return 
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE author ILIKE %s",
        (author,))
    books = cursor.fetchall()
    if books is None:
        print("Book not found")
    else:
        for id, title, author, genre, year, available in books:
            display_book(title, author, genre, year, available)

def search_by_genre():
    genre = user_input("Enter genre (press x to cancel): ")
    if genre is None:
        return 
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute(
        "SELECT * FROM books WHERE genre ILIKE %s",
        (genre,))
    books = cursor.fetchall()
    if books is None:
        print("Book not found")
    else:
        print(f"\n --- {genre} ---")
        for id, title, author, genre, year, available in books:
            display_book(title, author, genre, year, available)

def search_book():
    while True:
        search_menu()
        choice = get_menu_choice("Select Option (1/2/3/4): ")
        if choice == 1:
            search_by_title()
        elif choice == 2:
            search_by_author()
        elif choice == 3:
            search_by_genre()
        elif choice == 4:
            print("Exiting...")
            break 

def view_books_menu():
    print("\n --- View Books ---")
    print("1.View all books")
    print("2.View Available Books")
    print("3.View Borrowed Books")
    print("4.Exit")

def view_all_books():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()
    print("--- All Books ---")
    for id, title, author, genre, year, available in books:
        display_book(title, author, genre, year, available)
    
    cursor.close()
    connection.close()

def view_available_books():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM  books WHERE available = True")
    books = cursor.fetchall()
    print("\n --- Available Books ---")
    for id, title, author, genre, year, available in books:
        display_book(title, author, genre, year, available)

        cursor.close()
        connection.close()

def view_borrowed_books():
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books WHERE available = False")
    books = cursor.fetchall()
    print("\n --- Borrowed Books ---")
    for id, title, author, genre, year, available in books:
        display_book(title, author, genre, year, available)

        cursor.close()
        connection.close()

def view_books():
    while True:
        view_books_menu()
        choice = get_menu_choice("Please Select Option (1/2/3/4): ")
        if choice == 1:
            view_all_books()
        elif choice ==2:
            view_available_books()
        elif choice == 3:
            view_borrowed_books()
        elif choice == 4:
            print("Exiting...")
            break 

def add_book():
    title = user_input("Enter Book Title:  (press X to cancel)")
    if title is None:
        return  
    author = user_input("Enter Author:  (press X to cancel)")
    if author is None:
        return
    genre = user_input("Enter Genre:  (press X to cancel)")
    if genre is None:
        return
    year = get_int_value("Enter Year: ")
    if year is None:
        return 
    
    connection = connect_database()
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM books" \
    " WHERE title ILIKE %s" \
    " AND author ILIKE %s",
     (title, author))
    book = cursor.fetchone()
    if book:
        print("Book already exists!")
        cursor.close()
        connection.close()
        return
    
    
    cursor.execute("INSERT INTO books " \
        " (title, author, genre, year, available)" \
        " VALUES" \
        " (%s, %s, %s, %s, %s)",
         (title, author, genre, year, True))
    connection.commit()
    print("Book has been successfully added!")
    
    cursor.close()
    connection.close()



def borrow_book():
    title = user_input("Enter Book Title:    (press X to cancel)")
    if title is None:
        return
    
    connection = connect_database()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM books" \
    " WHERE title ILIKE %s", 
     (title,))
    book = cursor.fetchone()
    if book is None:
        print("book does not exist!")
        return 
    id, title, author, genre, year, available = book
    if not available:
        print("Book Already Borrowed")

        cursor.close()
        connection.close()
        return 
    
    display_book(title, author, genre, year, available)
    confirm = get_confirmation("Confirm this book (Y/N): ")
    if not confirm:
        print("Borrow Cancelled!")
        cursor.close()
        connection.close()
        return 
    
    cursor.execute("UPDATE books SET available = False" \
    " WHERE id = %s",
     (id, ))
    connection.commit()
    print("Book Borrowed Successfully!")
    
def return_book():
    title = user_input("Enter Book Title:    (press X to cancel)")
    if title is None:
        return
    
    connection = connect_database()
    cursor = connection.cursor()
    
    cursor.execute("SELECT * FROM books " \
    " WHERE title ILIKE %s",
     (title,))
    book = cursor.fetchone()
    if book is None:
        print("Book does not exist!")
        cursor.close()
        connection.close()
        return
    
    
    id, title, author, genre, year, available = book
    if available:
        print("Book has already been returned!")

    display_book(title, author, genre, year, available)
    confirm = get_confirmation("Please confirm (Y/N): ")
    if not confirm:
        print("Return has been cancelled")
        cursor.close()
        connection.close()
        return
    
    cursor.execute("UPDATE books" \
    " SET available = True" \
    " WHERE id = %s ",
     (id,))

    connection.commit()
    print("Book has been returned successfully!")

    cursor.close()
    connection.close()
    return 


def delete_book():
    title = input("Enter Title (press X to cancel): ")
    if title is None:
        return 
    
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM books" \
    " WHERE title ILIKE %s",
     (title,))
    book = cursor.fetchone()
    if book is None:
        print("Book does not exist!")
        return 
    
    id, title, author, genre, year, available = book
    display_book(title, author, genre, year, available)
    confirm = get_confirmation("Please Confirm (Y/N): ")
    if not confirm:
        print("Cancelling...")
        cursor.close()
        connection.close()
        return 
    
    cursor.execute("DELETE FROM books" \
    " WHERE id = %s",
     (id,))
    
    connection.commit()
    print("Book has been successfully deleted!")

    cursor.close()
    connection.close()


if __name__ == "__main__":
   search_book()