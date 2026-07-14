from library import borrow_book, return_book, view_books, add_book
from books_data import library 
from search_books import search_book

def user_menu():
    print("\n --- Library --- ")
    print("1.View Books")
    print("2.Add Book")
    print("3.Borrow Book")
    print("4.Return Book")
    print("5.Search Book")
    print("6.Exit")

def get_choice():
    choice = int(input("Select Option (1/2/3/4/5/6): "))
    return choice 



def main():
    while True:
        user_menu()
        choice = get_choice()
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
            print("Exiting")
            break 


if __name__ == "__main__":
    main()