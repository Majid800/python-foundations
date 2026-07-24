"""
Book Class

This module contains the Book class, which represents a single book
within the Library Management System.

Book objects are created from PostgreSQL database records and
store the details of one book while the application is running.
"""



class Book:
    """
    Represents a single book in the library.

    A Book object stores the details of one book retrieved
    from the PostgreSQL database.
    """
    
    def __init__(self, title, author, genre, year, available = True):
        """
        Initialise a new Book object.

        Stores the title, author, genre, publication year and
        availability status for a single book.
        """
        
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = available                                             
        
    def display_book(self):
        """
        Display the book's information.

        Prints the title, author, genre, publication year and
        current availability status in a readable format.
        """

        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Year: {self.year}")
        status = "Available" if self.available else "Borrowed"
        print(f"status: {status}")

    