#Library 
from validations import get_int_value, user_input, get_confirmation, get_menu_choice
from storage import save_library

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

#HELPER FUNCTIONS
def display_book(title,info):
    """
    Displays the details of the specified book.

    Searches the library for the given book title, displays its
    details if found, and returns the book's information.
    Returns None if the book does not exist.
    """
    print(f"\nTitle: {title}")
    print(f"Author: {info['author']}")
    print(f"Genre: {info['genre']}")
    print(f"Year: {info['year']}")
    status = "Available" if info['available'] else "Borrowed"
    print(f"status: {status}")
     
    

        


#MAIN FUNCTIONS 
def add_book(library):
    """
    Adds a new book to the library.

    Collects and validates user input before storing the
    book's details with an available status.
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
    year = get_int_value("Enter Year (press X to cancel): ")
    if year is None:
        return 

    if title in library:
        print("Book Already Exists!")
    else:
        library[title] = {
            "author": author,
            "genre": genre,
            "year": year,
            "available": True
            }
        save_library(library)
        print("Book Added Succesfully!")
        



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


def search_book(library):
    """
    Searches the library for books.

    Supports searching by title, author, or genre
    and displays any matching results.
    """
    while True:
        search_menu()
        choice = get_menu_choice("Please Select choice (1/2/3/4): ")
        if choice ==1:
            title = user_input("Enter Book Title (press X to cancel): ")
            if title is None:
                return
            if title in library:
                info = library[title]
                print("\n --- Books ---")
                display_book(title,info)
            else:
                print("Book does not exist!")
        elif choice == 2:
            author = user_input("Enter Author (press X to cancel): ")
            if author is None:
                return
            found = False
            print("\n --- Books ---")
            for title, info in library.items():
                if author == info["author"]:
                    found = True
                    display_book(title,info)
            if not found:
                print("Book does not exist!")
        elif choice == 3:
            genre = user_input("Enter Genre (press X to cancel): ")
            if genre is None:
                return 
            found = False
            print("\n --- Books ---")
            for title, info in library.items():
                if genre == info["genre"]:
                    found = True
                    display_book(title,info)
            if not found:
                print("Books does not exist!")
        elif choice ==4:
            print("Exiting...")
            break



def view_books_menu():
    """
    Displays the view books menu.

    Allows the user to choose how they would like
    to view the library collection.
    """
    print("\n --- View Books ---")
    print("1.View all books")
    print("2.View Available Books")
    print("3.View Borrowed Books")
    print("4.Exit")

def view_books(library):
    """
    Displays books from the library.

    Supports viewing all books, available books,
    or borrowed books based on the selected filter.
    """
    while True:
        view_books_menu()
        choice = get_menu_choice("Please Select Option (1/2/3/4): ")
        if choice ==1:
            print("\n ---- Books ----")
            for title, info in library.items():
                display_book(title,info)
        elif choice == 2:
            print("\n --- Available Books ---")
            for title,info in library.items():
                if info['available']:
                    print(title)
        elif choice ==3:
            print("\n --- Borrowed Books ---")
            for title,info in library.items():
                if not info['available']:
                    print(title)
        elif choice == 4:
            print("exiting...")
            break 



def borrow_book(library):
    """
    Borrows a book from the library.

    Displays the selected book, confirms the user's
    choice, and updates its availability status.
    """
    title_input = user_input("Enter Book Title (press X to cancel): ")
    if title_input is None:
        return
    for title, info in library.items():
        if title_input == title:
             display_book(title,info)
    if info is None:
        return
    confirm = get_confirmation("Confirm this book (Y/N): ")
    if confirm:
        if info["available"]:
            info["available"] = False
            save_library(library)
            print("Book has been successfully borrowed!")
                
        else:
            print("Book already borrowed")
    else:
            print("Cancelled")

def return_book(library):
    """
    Returns a borrowed book to the library.

    Displays the selected book, confirms the user's
    choice, and updates its availability status.
    """
    input_title = user_input("Enter Book Title:   (press X to cancel) ")
    if input_title is None:
        return
    for title, info in library.items():
         if input_title == title:
              display_book(title,info)
    confirm = get_confirmation("Confirm this book (Y/N): ")
    if confirm:
        if info["available"] == True:
                print("Book has already been returned")
        else:
                info["available"] = True
                save_library(library)
                print("Book has been successfully Returned!")
    else:
        print("Cancelled")


def delete_book(library):
    """
    Deletes a book from the library.

    Removes the selected book if it exists.
    """
    title =  user_input("Enter Book Title (press X to cancel): ")
    if title is None:
        return
    if title in library:
        del library[title]
        print("Book has been deleted!")
        save_library(library)
    else: 
        print("Book does not exist!")


if __name__ == "__main__":
   search_book()