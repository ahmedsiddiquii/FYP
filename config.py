import pymysql


def mysqlconnect(username = None,password = None,host = None,port = None,dbname = None):
    # To connect MySQL database
    if username == None:
        conn = pymysql.connect(
            host='localhost',
            user='root',
            password="12345678",
            db="test"
        )
    else:
        try:
            conn = pymysql.connect(
                host= host,
                user= username,
                password= password,
                db= dbname,
            )
        except:
            conn = pymysql.connect(
                host=host,
                user=username,
                password=password

            )
            q = f"CREATE DATABASE {dbname}"
            cursor = conn.cursor()
            cursor.execute(q)
            conn.commit()

            conn = pymysql.connect(
                host=host,
                user=username,
                password=password,
                db=dbname,
            )


    return conn

    # cur = conn.cursor()
    # cur.execute("select @@version")
    # output = cur.fetchall()
    # print(output)
    #
    # # To close the connection
    # conn.close()


