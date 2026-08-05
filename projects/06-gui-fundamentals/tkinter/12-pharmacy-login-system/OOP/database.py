import psycopg

def connect_database():
    connection = psycopg.connect(
             dbname = "pharmacy_system",
             user = "postgres",
             password = "King1978!", 
             host = "localhost",
             port = "5432")
    cursor = connection.cursor()
     
    return connection, cursor  

def check_login(username,password):
    connection, cursor  = connect_database()

    cursor.execute("SELECT username, password" \
    " FROM users" \
    " WHERE username = %s",
     (username,))

    row = cursor.fetchone()
    if row is None:

        cursor.close()
        connection.close()
        return "user_not_found"
 
    
    username_db, password_db = row
    if password_db == password:
        return "Login Successful"

    else:
        return "password does not match" 
