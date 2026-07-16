
from books_data import library 
from validations import get_non_empty_input, get_menu_choice

def search_menu():
    print("\n --- Search Book ---")
    print("1. Search by Title")
    print("2. Search by Author")
    print("3. Search by Genre")



def search_book():
    search_menu()
    choice = get_menu_choice("Please Select choice (1/2/3): ")
    if choice ==1:
        title = get_non_empty_input("Enter Book Title: ")
        if title in library:
            print("\n --- Book Details ---")
            info = library[title]
            print(f"Title: {title}")
            print(f"Author: {info['author']}")
            print(f"Genre: {info['genre']}")
            print(f"Year: {info['year']}")
            status = "Available" if info['available'] else "Borrowed"
            print(f"status: {status}")
            print("-"*20)
        else:
            print("Book does not exist!")
    elif choice == 2:
        author = get_non_empty_input("Enter Author: ")
        print("\n --- Book Details ---")
        found = False
        for title, info in library.items():
            if author == info["author"]:
                found = True
                print(f"Title: {title}")
                print(f"Author: {info['author']}")
                print(f"Genre: {info['genre']}")
                print(f"Year: {info['year']}")
                status = "Available" if info['available'] else "Borrowed"
                print(f"status: {status}")
                print("-"*20)
        if not found:
            print("Book does not exist")
    elif choice == 3:
        genre = get_non_empty_input("Enter Genre: ")
        found = False
        for title, info in library.items():
            if genre == info["genre"]:
                found = True
                print(f"Title: {title}")
                print(f"Author: {info['author']}")
                print(f"Genre: {info['genre']}")
                print(f"Year: {info['year']}")
                status = "Available" if info['available'] else "Borrowed"
                print(f"status: {status}")
                print("-"*20)
        if not found:
            print("Books does not exist!")

if __name__ == "__main__":
    search_book()