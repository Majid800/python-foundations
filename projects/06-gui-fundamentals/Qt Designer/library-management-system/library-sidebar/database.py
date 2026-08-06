import psycopg

def connect_database():
    connection = psycopg.connect(
             dbname = "library_management",
             user = "postgres",
             password = "King1978!", 
             host = "localhost",
             port = "5432")
    cursor = connection.cursor()
     
    return connection, cursor  

def get_books():
    connection, cursor = connect_database()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    cursor.close()
    connection.close()
    return books

def get_books_by_genre(genre):
    connection, cursor = connect_database()

    cursor.execute("SELECT * FROM books" \
    " WHERE genre = %s",
     (genre,))

    books = cursor.fetchall()

    cursor.close()
    connection.close()
    return books

def get_available_books(available):
    connection, cursor = connect_database()

    cursor.execute("SELECT * FROM books" \
    " WHERE available = %s",
     (available,))

    books = cursor.fetchall()
    
    cursor.close()
    connection.close()
    return books