import psycopg 
"""
Storage Module

Handles communication with the PostgreSQL database.

Provides functionality for establishing database
connections used throughout the application.

Responsibilities:
- Connect to the PostgreSQL database.
- Return a database connection object.
"""

def connect_database():
    """
    Creates and returns a connection to the PostgreSQL database.

    Uses psycopg to connect to the library_management database
    on the local PostgreSQL server.
    """
     
    connection = psycopg.connect(
        dbname = "library_management",
        user = "postgres",
        password = "King1978!", 
        host = "localhost",
        port = "5432")
    return connection 
