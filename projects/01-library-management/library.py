#Library 
from books_data import library 
from validations import get_int_value, user_input, get_confirmation, display_book

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
    title = user_input("Enter Book Title:    (press X to cancel)")
    if title is None:
        return
    info = display_book(title)
    if info is None:
        return
    confirm = get_confirmation("Confirm this book (Y/N): ")
    if confirm:
        if info["available"]:
            info["available"] = False
            print("Book has been successfully borrowed!")
                
        else:
            print("Book already borrowed")
    else:
            print("Cancelled")

def return_book():
    title = user_input("Enter Book Title:   (press X to cancel) ")
    if title is None:
        return 
    info = display_book(title)
    confirm = get_confirmation("Confirm this book (Y/N): ")
    if confirm:
        if info["available"] == True:
                print("Book has already been returned")
        else:
                info["available"] = True
                print("Book has been Returned!")
    else:
        print("Cancelled")
    

def delete_book():
    title =  user_input("Enter Book Title:     (press X to cancel)")
    if title is None:
        return
    if title in library:
        del library[title]
        print("Book has been deleted!")
    else: 
        print("Book does not exist!")


if __name__ == "__main__":
    borrow_book()