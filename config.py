import pymysql


def mysqlconnect():
    # To connect MySQL database
    try:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="Ahmed12345",
            db='test',
        )
    except:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="Ahmed12345@",
        )
    return conn

    # cur = conn.cursor()
    # cur.execute("select @@version")
    # output = cur.fetchall()
    # print(output)
    #
    # # To close the connection
    # conn.close()


