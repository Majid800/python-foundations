#Library 
from books_data import library 
from validations import get_int_value, get_non_empty_input 

def add_book():
    title = get_non_empty_input("Enter Book Title: ")
    author = get_non_empty_input("Enter Author: ")
    genre = get_non_empty_input("Enter Genre: ")
    year = get_int_value("Enter Year: ")

    if title in library:
        print("Book Already Exists!")
    else:
        library[title] = {
            "author": author,
            "genre": genre,
            "year": year,
            "available": True
            }
        print("Book Added Succesfully!")



def view_books():
    if not library:
        print("no books found")
    else:
        print("\n ---- Books ----")
        for title, info in library.items():
            print(f"Title: {title}")
            print(f"Author: {info['author']}")
            print(f"Genre: {info['genre']}")
            print(f"Year: {info['year']}")
            status = "Available" if info['available'] else "Borrowed"
            print(f"status: {status}")
            print("-"*20)

def borrow_book():
    title = get_non_empty_input("Enter Book Title: ")
    if title in library:
        info = library[title]
        print("\n --- Books ---")
        print(f"Title: {title}")
        print(f"Author: {info['author']}")
        print(f"Genre: {info['genre']}")
        print(f"Year: {info['year']}")
        print(f"Available: {info['available']}")
        confirm = input("Confirm this book (Y/N): ").strip().upper()
        if confirm == 'Y':
            if info["available"]:
                info["available"] = False
                print("Book has been successfully borrowed!")
                
            else:
                print("Book already borrowed")
        else:
            print("Cancelled")
    else:
        print("Book does not exist!")

def return_book():
    title = get_non_empty_input("Enter Book Title: ")
    if title in library:
        info = library[title]
        print("\n --- Books ---")
        print(f"Title: {title}")
        print(f"Author: {info['author']}")
        print(f"Genre: {info['genre']}")
        print(f"Year: {info['year']}")
        print(f"Available: {info['available']}")
        confirm = input("Confirm this book (Y/N): ").strip().upper()
        if confirm == 'Y':
            if info["available"] == True:
                print("Book has already been returned")
            else:
                info["available"] = True
                print("Book has been succesfuly borrowed!")
        else:
            print("Cancelled")
    else:
        print("Book not found")

def delete_book():
    title =  get_non_empty_input("Enter Book Title: ")
    if title in library:
        del library[title]
        print("Book has been deleted!")
    else: 
        print("Book does not exist!")

