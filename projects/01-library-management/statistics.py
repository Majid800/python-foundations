from books_data import library 
from validations import get_menu_choice

# Displays a summary of the library by showing the total number of books,
# available books, and borrowed books. Calculates all statistics in a
# single loop through the library for improved efficiency.


def statistics_menu():
    print("\n --- Library Statistics ---")
    print("1.Overall Statistics")
    print("2.Books by Genre")
    print("3.Books by Author")
    print("4.Exit")







def Overall_statistics():
    total = len(library)
    available = 0
    borrowed = 0
    for title, info in library.items():
        if info['available'] == True:
            available += 1
        elif info['available'] == False:
            borrowed = 0+1 
    print("\n --- Library statistics ---")
    print(f"Total Books: {total}")
    print(f"Available Books: {available}")
    print(f"Borrowed Books: {borrowed}")


genre_count = {}

def books_by_genre():
    for title, info in library.items():
        genre = info["genre"]
        if genre in genre_count:
            genre_count[genre] +=1
        else:
            genre_count[genre] = 1
        for genre, count in genre_count.items():
            print(f"{genre}: {count}")

author_count = {}

def books_by_author():
    for title, info in library.items():
        author = info["author"]
        if author in author_count:
            author_count[author] +=1
        else:
            author_count[author] = 1
        for author, count in author_count.items():
            print(f"{author}: {count}")

def main():
    while True:
        statistics_menu()
        choice = get_menu_choice("Please Select Option (1/2/3/4):  ")
        if choice == 1:
            Overall_statistics()
        elif choice == 2:
            books_by_genre()
        elif choice == 3:
            books_by_author()
        elif choice == 4:
            print("Exiting...")
            break 

if __name__ =="__main__":
    main()