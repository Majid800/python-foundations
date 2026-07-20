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

    Reads the contents of 'books.json' and converts the JSON
    data into a Python dictionary.

    If the file does not exist or contains invalid JSON,
    an empty library is returned and a message is displayed
    to the user.

    Returns:
        dict: A dictionary containing all books in the library.
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

    Converts the Python dictionary into JSON format and
    writes it to 'books.json'. Existing file contents are
    overwritten with the updated library data.

    The JSON file is formatted with indentation for readability
    and preserves non-ASCII characters.

    Args:
        library (dict): The library dictionary to be saved.
    """
    with open("books.json", "W") as file:
        json.dump(library, file, indent=4, ensure_ascii=False)