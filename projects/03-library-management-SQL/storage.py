import psycopg 

def connect_database():
    connection = psycopg.connect(
        dbname = "library_management",
        user = "postgres",
        password = "King1978!", 
        host = "localhost",
        port = "5432")
    return connection 
