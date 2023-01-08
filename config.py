import pymysql


def mysqlconnect():
    # To connect MySQL database
    conn = pymysql.connect(
        host='localhost',
        user='root',
        password="12345678",
        db='AutomativeDatabse',
    )

    return conn

    # cur = conn.cursor()
    # cur.execute("select @@version")
    # output = cur.fetchall()
    # print(output)
    #
    # # To close the connection
    # conn.close()


