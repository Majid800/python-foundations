import psycopg 
"""
Database Connection

This module is responsible for establishing a connection to the
PostgreSQL database used by the Library Management System.

It provides a reusable function that returns both the database
connection and cursor required to execute SQL queries.
"""

def connect_database():
    """
    Creates and returns a connection to the PostgreSQL database.

    Uses psycopg to connect to the library_management database
    on the local PostgreSQL server. Then returns
    both so that SQL queries can be executed by the Library
    class.
    """
     
    connection = psycopg.connect(
        dbname = "library_management",
        user = "postgres",
        password = "King1978!", 
        host = "localhost",
        port = "5432")
    cursor = connection.cursor()

    return connection, cursor  

    