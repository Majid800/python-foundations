import json 

"""
Storage Module

Handles loading and saving the library data.

Reads the library data from books.json, converts it into a Python
dictionary for use throughout the application, and saves any changes
back to the JSON file.
"""

def load_library():
    with open("books.json") as file:
        library = json.load(file)
    return library 

def save_library(library):
    with open("books.json", "W") as file:
        json.dump(library, file)