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


def get_books_by_keyword(keyword):
    connection, cursor = connect_database()

    keyword = f"%{keyword}%"
    cursor.execute("SELECT * FROM books" \
    " WHERE title ILIKE %s" \
    " OR author ILIKE %s" \
    " OR genre ILIKE %s" \
    " OR CAST(year AS TEXT) ILIKE %s",
     (keyword, keyword, keyword, keyword))

    books = cursor.fetchall()

    cursor.close()
    connection.close()
    return books

def book_borrowed(book_id):
    connection, cursor = connect_database()

    cursor.execute("SELECT * FROM books " \
    " WHERE id = %s" \
    " and available = TRUE",
     (book_id,))

    book = cursor.fetchone()
    if book is None:
        cursor.close()
        connection.close()
        return False
    else:
        cursor.execute("UPDATE books" \
        " SET available = FALSE" \
        " where id = %s",
         (book_id,))

        connection.commit()
        cursor.close()
        connection.close()
        return True 

def book_returned(book_id):
    connection, cursor = connect_database()
    
    cursor.execute("SELECT * FROM books " \
    " WHERE id = %s" \
    " and available = FALSE",
     (book_id,))

    book = cursor.fetchone()
    if book is None:
        cursor.close()
        connection.close()
        return False 

    else:
        cursor.execute("UPDATE books" \
        " SET available = TRUE" \
        " where id = %s",
         (book_id,))
        
        connection.commit()
        cursor.close()
        connection.close()
        return True


# Dasboard Overview 

def get_total_books_count():
    connection, cursor = connect_database()

    cursor.execute(" SELECT COUNT(*) FROM books")

    result = cursor.fetchone()
    total_books = result[0]

    cursor.close()
    connection.close()
    return total_books



def get_available_books_count():
    connection, cursor = connect_database()
    cursor.execute(" SELECT COUNT(*) FROM books" \
    " WHERE available = TRUE")

    result = cursor.fetchone()
    total_available_books = result[0]

    cursor.close()
    connection.close()
    return total_available_books




def get_borrowed_books_count():
    connection, cursor = connect_database()
    cursor.execute(" SELECT COUNT(*) FROM books" \
    " WHERE available = FALSE")

    result = cursor.fetchone()
    total_borrowed_books = result[0]
    
    cursor.close()
    connection.close()
    return total_borrowed_books
    
def get_genre_count():
    connection, cursor = connect_database()

    cursor.execute("SELECT genre, COUNT(*)" \
    " FROM books" \
    " GROUP BY genre;")

    genre_counts = cursor.fetchall()

    cursor.close()
    connection.close()
    return genre_counts

def get_trending_genres():
    connection, cursor = connect_database()

    cursor.execute("SELECT genre, COUNT(*)" \
    " FROM books " \
    " WHERE available = False" \
    " GROUP BY genre;")

    trending_genres = cursor.fetchall()

    cursor.close()
    connection.close()
    return trending_genres




    

        


    
    