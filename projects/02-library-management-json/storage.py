import json 

"""
Storage Module

Handles loading and saving the library data.

Reads the library data from books.json, converts it into a Python
dictionary for use throughout the application, and saves any changes
back to the JSON file.
"""

def load_library():
    try:
        with open("books.json") as file:
            library = json.load(file)
            return library
    except FileNotFoundError:
        print("Library Data Not Found")
        print("Starting with new libary data")
        return {}
    except json.JSONDecodeError:
        print("Library Data Corrupted")
        print("Starting with new library data")
        return {}


def save_library(library):
    with open("books.json", "W") as file:
        json.dump(library, file, indent=4, ensure_ascii=False)