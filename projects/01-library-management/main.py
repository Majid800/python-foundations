from library import borrow_book, return_book, view_books, add_book, search_book
from books_data import library 
from validations import get_menu_choice
from statistics import search_by_statistics




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
            add_book()
        elif choice == 3:
            borrow_book()
        elif choice == 4:
            return_book()
        elif choice == 5:
            search_book()
        elif choice == 6:
            search_by_statistics()
        elif choice == 7:
            print("Exiting")
            break 


if __name__ == "__main__":
    main()