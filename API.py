from config import mysqlconnect
import sqlite3

def connect_default():
    try:
        conn = sqlite3.connect('automativedatabase.db')
        print("Connected to SQLite3 database 'automativedatabase'")

        # Check if the 'user' table exists, and create it if not
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='user'")
        if cursor.fetchone() is None:
            query = '''CREATE TABLE user (
                        id INTEGER NOT NULL PRIMARY KEY,
                        username VARCHAR(255) NOT NULL,
                        password VARCHAR(255) NOT NULL,
                        name VARCHAR(255) NOT NULL)'''
            cursor.execute(query)
            conn.commit()
            print("Table 'user' created successfully")

        return conn
    except sqlite3.Error as e:
        print(f"An error occurred while connecting to the database: {e}")
        return None
def auth (username, password):
    try:
        print(username)
        print(password)
        connection = connect_default()
        cursor = connection.cursor()

        query = "select * from user where username = ?"
        cursor.execute(query,(username,))
        data = list(cursor.fetchall())
        print(data)
        db_password = data[0][2]
        if password==db_password:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
def add_user(user,password):
    query = f"insert into user(username,password,name) values('{user}','{password}','{user}')"
    conn = connect_default()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        conn.commit()
        print("inserted")
    except Exception as e:
        print(e)
def initializeDB():
    query = 'CREATE DATABASE AutomativeDatabse'
    conn = mysqlconnect()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
    except Exception as e:
        print(e)

    query = 'CREATE TABLE user (id INT NOT NULL AUTO_INCREMENT,username VARCHAR(255) NOT NULL,password VARCHAR(255) NOT NULL,name VARCHAR(255) NOT NULL,PRIMARY KEY (id))'
    conn = mysqlconnect()
    try:
        cursor = conn.cursor()
        cursor.execute(query)
        query = "insert into user(username,password,name) values('admin','admin','admin')"
        conn = mysqlconnect()
        try:
            cursor = conn.cursor()
            cursor.execute(query)
            conn.commit()
            print("inserted")
        except Exception as e:
            print(e)
    except Exception as e:
        print(e)



# print(auth("admin","admin"))

