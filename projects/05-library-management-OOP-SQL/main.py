from book import Book
from library import Library
from validations import get_menu_choice

"""
Main Application

Starts the application and launches the main menu.
This file keeps program startup separate from the rest
of the application logic.
"""

test_library = Library()

def user_menu():
    """
    Displays the main library menu.

    Presents the available library management options
    to the user.
    """
    print("\n --- Library --- ")
    print("1.View Books")
    print("2.Add Book")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Search Book")
    print("6.Library Statistics")
    print("7.Exit")

def view_books_menu():
    print("\n --- View Books ---")
    print("1.View All Books")
    print("2.View Avaialable Books")
    print("3.View Borrowed Books")
    print("4.Exit")

def view_books():
    while True:
        view_books_menu()
        choice = get_menu_choice("Select Option (1/2/3/4): ")
        if choice == 1:
            test_library.view_all_books()
        elif choice == 2:
            test_library.view_available_books()
        elif choice == 3:
            test_library.view_borrowed_books()
        elif choice == 4:
            print("Exiting...")
            break 

def search_books_menu():
    print("\n --- Search Books ---")
    print("1.Search By Title")
    print("2.Search by Author")
    print("3.Search by Genre")
    print("4.Exit")

def search_books():
    while True:
        search_books_menu()
        choice = get_menu_choice("Select Option (1/2/3/4): ")
        if choice == 1:
            test_library.search_by_title()
        elif choice == 2:
            test_library.search_by_author()
        elif choice == 3:
            test_library.search_by_genre()
        elif choice == 4:
            print("Exiting...")
            break 


def statistics_menu():
    print("\n --- Statistics ---")
    print("1.Overall Statistics")
    print("2.Books by Genre")
    print("3.Books by Author")
    print("4.Exit")

def search_statistics():
    while True:
        statistics_menu()
        choice = get_menu_choice("Please Enter option (1/2/3/4): ")
        if choice == 1:
            test_library.overall_statistics()
        elif choice == 2:
            test_library.books_by_genre()
        elif choice == 3:
            test_library.books_by_author()
        elif choice == 4:
            print("Exiting...")
            break 



def main():
    """
    Runs the main application loop.

    Processes the user's menu selection and calls the
    appropriate library management function until the
    user chooses to exit.
    """
    while True:
        user_menu()
        choice = get_menu_choice("Please Select Option (1/2/3/4/5/6/7): ")
        if choice ==1:
            view_books()
        elif choice == 2:
            test_library.add_book()
        elif choice == 3:
            test_library.borrow_book()
        elif choice == 4:
            test_library.return_book()
        elif choice == 5:
            search_books()
        elif choice == 6:
           search_statistics()
        elif choice == 7:
            print("Exiting")
            break 


if __name__ == "__main__":
    main()