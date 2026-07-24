#creating book class 

class Book:
    def __init__(self, title, author, genre, year, available=True):
        self.title = title
        self.author = author
        self.genre = genre
        self.year = year
        self.available = available                                             

    def display_book(self):
        print(f"\nTitle: {self.title}")
        print(f"Author: {self.author}")
        print(f"Genre: {self.genre}")
        print(f"Year: {self.year}")
        status = "Available" if self.available else "Borrowed"
        print(f"status: {status}")

    

