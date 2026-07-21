#creates library class that has the list of books inside and performs functions to the books
from book import Book
from validations import user_input, get_int_value, get_confirmation

class Library:
    def __init__(self):
        self.books = []
    
    def add_book(self):
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
        for book in self.books:
            book.display_book()

    def view_available_books(self):
        print("\n--- Available Books ---")
        for book in self.books: 
            if book.available:
                book.display_book()
    
    def view_borrowed_books(self):
        print("\n--- Borrowed Books ---")
        for book in self.books():
            if not book.available:
                book.display_book()

    def search_by_title(self):
        title = user_input("Please enter Title: (press X to cancel): ")
        if title is None:
            return
        
        for book in self.books:
            if title == book.title:
                book.display_book()
                return
            
        print("Book does not exist!")

    def search_by_author(self):
        author = user_input("Please Enter Author: (press X to cancel): ")
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
        genre = user_input("Please Enter Genre: (press X to cancel): ")
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
        title = user_input("Please enter Title: (press X to cancel): ")
        if title is None:
            return
        author = user_input("Please enter Author: (press X to cancel): ")
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
        title = user_input("Please enter Title: (press X to cancel): ")
        if title is None:
            return
        author = user_input("Please enter Author: (press X to cancel): ")
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
        title = user_input("Please enter Title: (press X to cancel): ")
        if title is None:
            return
        author = user_input("Please enter Author: (press X to cancel): ")
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
        author_count = {}
        for book in self.books:
            author = book.author 
            if author in author_count:
                author_count[author] +=1
            else:
                author_count[author] = 1
            
            for author, count in author_count.items():
                print(f"{author}: {count}")


