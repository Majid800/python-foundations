from validations import get_menu_choice

"""
Library Statistics Module

Provides statistical reports for the library including overall
book totals, books grouped by genre, and books grouped by author.

The library dictionary is received as a parameter rather than
being imported directly. This separates the statistics logic
from the data storage layer, allowing the module to work with
data loaded from JSON and making the application easier to
maintain and extend.
"""

def statistics_menu():
    """
    Displays the library statistics menu.

    Allows the user to choose which statistics
    report they would like to view.
    """
    print("\n --- Library Statistics ---")
    print("1.Overall Statistics")
    print("2.Books by Genre")
    print("3.Books by Author")
    print("4.Exit")







def Overall_statistics(library):
    """
    Displays an overview of the library.

    Shows the total number of books along with
    the available and borrowed book counts.
    """
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




def books_by_genre(library):
    """
    Groups books by genre.

    Counts and displays the total number of
    books in each genre.
    """
    genre_count = {}
    for title, info in library.items():
        genre = info["genre"]
        if genre in genre_count:
            genre_count[genre] +=1
        else:
            genre_count[genre] = 1
        for genre, count in genre_count.items():
            print(f"{genre}: {count}")



def books_by_author(library):
    """
    Groups books by author.

    Counts and displays the total number of
    books written by each author.
    """
    author_count = {}
    for title, info in library.items():
        author = info["author"]
        if author in author_count:
            author_count[author] +=1
        else:
            author_count[author] = 1
        for author, count in author_count.items():
            print(f"{author}: {count}")

def search_by_statistics(library):
    """
    Runs the library statistics menu.

    Processes the user's selection and displays
    the requested statistics report.
    """
    while True:
        statistics_menu()
        choice = get_menu_choice("Please Select Option (1/2/3/4):  ")
        if choice == 1:
            Overall_statistics(library)
        elif choice == 2:
            books_by_genre(library)
        elif choice == 3:
            books_by_author(library)
        elif choice == 4:
            print("Exiting...")
            break 

    