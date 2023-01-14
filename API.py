from config import mysqlconnect
def auth (username, password):
    try:
        connection = mysqlconnect()
        cursor = connection.cursor()

        query = "select * from user where username = %s"
        cursor.execute(query,(username,))
        data = list(cursor.fetchall())
        db_password = data[0][1]
        if password==db_password:
            return True
        else:
            return False
    except:
        return False

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

