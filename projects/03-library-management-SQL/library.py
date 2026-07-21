#Library 
from validations import get_int_value, user_input, get_confirmation, get_menu_choice
from storage import connect_database

"""
Library Management Module

Contains the core business logic for the Library Management
System.

Provides functionality for viewing, searching, adding,
borrowing, returning and deleting books stored in a
PostgreSQL database.

Responsibilities:
- Display menus.
- Handle user interaction.
- Validate user input.
- Execute SQL queries through the storage layer.
- Display books and status messages.
"""

def display_book(title,author,genre, year, available):
    """
    Displays the details of a specified book.

    Formats and displays the information stored within a
    Book record, including title, author, genre, publication
    year and availability status.

    Args:
    title (str): Book title.
    author (str): Book author.
    genre (str): Book genre.
    year (int): Publication year.
    available (bool): Availability status.
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
    """
    Searches for a book by title.

    Retrieves the first matching book from the PostgreSQL
    database and displays its details if found.
    """
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
    """
    Searches for books by author.

    Retrieves all books written by the specified author
    and displays the matching results.
    """
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
    """
    Searches for books by genre.

    Retrieves all books matching the specified genre and
    displays the matching results.
    """
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
    """
    Runs the Search Books menu.

    Displays the search menu, processes the user's menu
    selection and executes the requested search operation
    until the user chooses to exit.
    """
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
    """
    Displays the View Books menu.

    Allows the user to choose whether to display all books,
    available books or borrowed books.
    """
    print("\n --- View Books ---")
    print("1.View all books")
    print("2.View Available Books")
    print("3.View Borrowed Books")
    print("4.Exit")

def view_all_books():
    """
    Displays all books in the library.

    Retrieves every book stored in the PostgreSQL database
    and displays each record to the user.
    """
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
    """
    Displays all available books.

    Retrieves books currently marked as available in the
    database and displays their details.
    """
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
    """
    Displays all borrowed books.

    Retrieves books currently marked as borrowed in the
    database and displays their details.
    """
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
    """
    Runs the View Books menu.

    Displays the View Books menu, processes the user's
    selection and executes the requested viewing operation
    until the user exits the menu.
    """
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
    """
    Adds a new book to the library.

    Collects book information from the user, validates the
    input, checks for duplicate books and inserts the new
    record into the PostgreSQL database if no duplicate
    exists.
    """
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
    """
    Borrows a book from the library.

    Searches for the requested book, verifies that it exists
    and is currently available, requests user confirmation
    and updates the database to mark the book as borrowed.
    """
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
    """
    Returns a borrowed book.

    Searches for the requested book, verifies that it exists
    and is currently borrowed, requests user confirmation
    and updates the database to mark the book as available.
    """
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
    """
    Deletes a book from the library.

    Searches for the requested book, displays its details,
    requests user confirmation and permanently removes the
    book from the PostgreSQL database.
    """
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