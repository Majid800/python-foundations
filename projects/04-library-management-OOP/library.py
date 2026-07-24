#creates library class that has the list of books inside and performs functions to the books
from book import Book
from validations import user_input, get_int_value, get_confirmation

"""
Library Class

This module contains the Library class, which manages a collection
of Book objects.

The Library class is responsible for adding, searching, borrowing,
returning, deleting and displaying books, as well as generating
library statistics.
"""

class Library:
    """
    Represents a library containing multiple Book objects.

    The Library class manages all operations performed on
    the collection of books.
    """

    def __init__(self):
        """
        Initialise an empty library.

        Creates a list used to store Book objects.
        """

        self.books = []
    
    def add_book(self):
        """
        Add a new book to the library.

        Collects book details from the user, creates a Book object,
        and stores it within the library collection.
        """

        title = user_input("Please enter Title: (press X to cancel): ")
        if title is None:
            return
        author = user_input("Please enter Author: (press X to cancel): ")
        if author is None:
            return 
        genre = user_input("Please enter genre: (press X to cancel): ")
        if genre is None:
            return
        year = get_int_value("Please enter year: (press X to cancel): ")
        if year is None:
            return
        available = True
        
        book = Book(title, author, genre, year, available)
        book.display_book()
        confirm = get_confirmation("Confirm this book (Y/N): ")
        if not confirm:
            print("Cancelling...")
            return 
        
        for existing_book in self.books:
            if book.title == existing_book.title and author.title == existing_book.author:
                print("Book already exists!")
                return 
            
        self.books.append(book)
        print("Book added successfully!")
        

    def view_all_books(self):
        """
        Display every book in the library.

        Iterates through the collection and displays each
        Book object's information.
        """

        for book in self.books:
            book.display_book()

    def view_available_books(self):
        """
        Display all available books.

        Shows every book that is currently marked as available.
        """

        print("\n--- Available Books ---")
        for book in self.books: 
            if book.available:
                book.display_book()
    
    def view_borrowed_books(self):
        """
        Display all borrowed books.

        Shows every book that is currently unavailable.
        """

        print("\n--- Borrowed Books ---")
        for book in self.books():
            if not book.available:
                book.display_book()

    def search_by_title(self):
        """
        Search for books by title.

        Displays all books written by the specified title.
        """

        title = user_input("Please enter Title: (press X to cancel): ")
        if title is None:
            return
        
        for book in self.books:
            if title == book.title:
                book.display_book()
                return
            
        print("Book does not exist!")

    def search_by_author(self):
        """
        Search for books by author.

        Displays all books written by the specified author.
        """

        author = user_input("Please Enter Author (press X to cancel): ")
        if author is None:
            return
        
        found = False
        print(f"\n --- {author} ---")
        for book in self.books:
            if author == book.author:
                found = True
                book.display_book()
                return
        if not found:
            print("Book does not exist!")

    def search_by_genre(self):
        """
        Search for books by genre.

        Displays all books that belong to the specified genre.
        """

        genre = user_input("Please Enter Genre (press X to cancel): ")
        if genre is None:
            return
        
        print(f"\n --- {genre} ---")
        found = False 
        for book in self.books:
            if genre == book.genre:
                found= True
                book.display_book()
        if not found: 
            print("book does not exist!")
            

    def borrow_book(self):
        """
        Borrow a book.

        Marks a selected available book as borrowed if it exists.
        """

        title = user_input("Please enter Title (press X to cancel): ")
        if title is None:
            return
        author = user_input("Please enter Author (press X to cancel): ")
        if author is None:
            return 
        
        found = False 

        for book in self.books:
            if title == book.title and author == book.author:
                found = True 
                book.display_book()
                confirm = get_confirmation("Do you want to borrow this book? (Y/N): ")
                if not confirm:
                    print("cancelling...")
                    return 
                
                if book.available:
                    book.available = False
                    print("Book has been successfully borrowed!")
                else:
                    print("book has already been borrowed!")
        if not found:
                print("Book does not exist!")
                    
    def return_book(self):
        """
        Return a borrowed book.

        Marks a selected borrowed book as available again.
        """

        title = user_input("Please enter Title (press X to cancel): ")
        if title is None:
            return
        author = user_input("Please enter Author (press X to cancel): ")
        if author is None:
            return

        found = False

        for book in self.books:
            if title == book.title and author == book.author:
                book.display_book()
                found = True 
                confirm = get_confirmation("Do you want to return this book? (Y/N): ")
                if not confirm:
                    print("cancelling...")
                    return  
            

                if book.available:
                    print("Book has already been returned!")
                else:
                    book.available = True
                    print("Book has been returned!")
        if not found:
            print("book does not exist!")


    def delete_book(self):
        """
        Delete a book from the library.

        Removes a selected book from the library collection.
        """

        title = user_input("Please enter Title (press X to cancel): ")
        if title is None:
            return
        author = user_input("Please enter Author (press X to cancel): ")
        if author is None:
            return
        
        found = False 

        for book in self.books():
            if title == book.title and author == book.author:
                found = True 
                book.display_book()
                confirm = get_confirmation("Do you want to delete this book? (Y/N): ")
                if not confirm:
                    print("cancelling...")
                    return
                
                self.books.remove(book)
                print("Book has been deleted!")
                return 
            
        if not found:
                print("Book does not exist!")


    #Statistics Operations 

    def overall_statistics(self):
        """
        Display overall library statistics.

        Shows the total number of books, available books
        and borrowed books.
        """

        total = len(self.books)
        available = 0 
        borrowed = 0 
        for book in self.books:
            if book.available:
                available +=1 
            else:
                borrowed +=1 
        print("\n --- Overall Statistics ---")
        print(f"Total: {total}")
        print(f"Available Books: {available}")
        print(f"Borrowed Books: {borrowed}")
        
    def books_by_genre(self):
        """
        Display the number of books in each genre.

        Counts and displays books grouped by genre.
        """
        genre_count ={}
        for book in self.books:
            genre = book.genre
            if genre in genre_count:
                genre_count[genre] += 1
            else:
                genre_count[genre] = 1
            for genre, count in genre_count.items():
                print(f"{genre}: {count}")
        
    def books_by_author(self):
        """
        Display the number of books written by each author.

        Counts and displays books grouped by author.
        """
        
        author_count = {}
        for book in self.books:
            author = book.author 
            if author in author_count:
                author_count[author] +=1
            else:
                author_count[author] = 1
            
            for author, count in author_count.items():
                print(f"{author}: {count}")


