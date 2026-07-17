from books_data import library 

# Displays a summary of the library by showing the total number of books,
# available books, and borrowed books. Calculates all statistics in a
# single loop through the library for improved efficiency.

def library_statistics():
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

library_statistics()
