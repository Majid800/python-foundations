from validations import get_menu_choice
from storage import connect_database

"""
Statistics Module

Provides statistical reports for the Library Management
System using SQL aggregation queries.

Responsibilities:
- Display the statistics menu.
- Generate summary reports.
- Execute SQL aggregation queries.
- Present statistical information to the user.
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

def overall_statistics():
    """
    Displays overall library statistics.

    Retrieves and displays the total number of books
    stored in the PostgreSQL database.
    """
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT COUNT(*)" \
    " FROM books")

    result = cursor.fetchone()
    count = result[0]

    print(f"Total Books: {count}")
    cursor.close()
    connection.close()

def books_by_author():
    """
    Displays the number of books written by each author.

    Uses SQL aggregation to group books by author and
    display the number of books within each group.
    """
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT author, COUNT(*)" \
    " FROM books" \
    " GROUP BY author" \
    " ORDER BY author")

    authors = cursor.fetchall()
    print("\n --- Books by Authors ---\n")
    for author, count in authors:
        print(f"{author}: {count}")

    cursor.close()
    connection.close()



def books_by_genre():
    """
    Displays the number of books in each genre.

    Uses SQL aggregation to group books by genre and
    display the number of books within each group.
    """
    connection = connect_database()
    cursor = connection.cursor()

    cursor.execute("SELECT genre, COUNT(*)" \
    " FROM books" \
    " GROUP BY genre" \
    " ORDER BY genre")

    genres = cursor.fetchall()
    for genre, count in genres:
        print(f"{genre}: {count}")

    cursor.close()
    connection.close()


def search_by_statistics():
    """
    Runs the Library Statistics menu.

    Processes the user's menu selection and displays
    the requested statistical report.
    """
    while True: 
        statistics_menu()
        choice = get_menu_choice("Please Enter Option (1/2/3/4): ")
        if choice ==1:
            overall_statistics()
        elif choice ==2:
            books_by_author()
        elif choice ==3:
            books_by_genre()
        elif choice == 4:
            print("Exiting...")
            break 