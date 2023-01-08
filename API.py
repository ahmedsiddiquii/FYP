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

# print(auth("admin","admin"))

