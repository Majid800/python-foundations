from books_data import library 

# Total Books
# Counts the total number of books currently stored in the library.
# Uses the length of the library dictionary.
# Displays the total number of books.

def total_books():
    total = len(library)
    print(f"Total Books: {total}")

# Available Books
# Iterates through every book in the library.
# Counts the number of books currently available.
# Displays the total number of available books.

def available_books():
    available = 0
    for title, info in library.items():
        if info['available'] == True:
            available = available + 1
    print(f"Available Books: {available}")



# Borrowed Books
# Iterates through every book in the library.
# Counts the number of books currently borrowed.
# Displays the total number of borrowed books.

def borrowed_books():
    borrowed = 0
    for title, info in library.items():
        if info['available'] == False:
            borrowed = borrowed +1
    print(f"Borrowed Books: {borrowed}")

       
# Library Statistics
# Displays an overview of the library.
# Calls each statistics function.
# Displays:
# - Total Books
# - Available Books
# - Borrowed Books

def library_statistics():
    print("\n ---- Library Statistics ---")
    total_books()
    available_books()
    borrowed_books()

