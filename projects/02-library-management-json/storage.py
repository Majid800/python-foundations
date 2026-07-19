import json 

"""
Storage Module

Handles loading and saving the library data.

Reads the library data from books.json, converts it into a Python
dictionary for use throughout the application, and saves any changes
back to the JSON file.

Provides a separation between the application's business logic and
its data storage, allowing the library to persist between program
sessions.
"""

def load_library():
    """
    Loads the library data from the JSON file.

    Opens books.json, converts the JSON data into a Python dictionary,
    and returns it for use throughout the application.

    If the JSON file is missing or contains invalid JSON, an empty
    dictionary is returned so the application can continue running
    without crashing.
    """
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
    """
    Saves the library data to the JSON file.

    Converts the current library dictionary into JSON format and
    writes it to books.json, preserving any additions, deletions,
    or updates made during the program.

    Formats the JSON using indentation for improved readability and
    preserves non-ASCII characters when saving.
    """

    with open("books.json", "W") as file:
        json.dump(library, file, indent=4, ensure_ascii=False)