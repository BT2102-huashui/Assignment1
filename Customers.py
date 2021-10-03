import pymysql
mysql_password = "ur password"

class Customer:
    def __init__(self) -> None:
        super().__init__()
        
    def login(self, userid, password):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=mysql_password, db='version2',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select password from customer where id = '%s'" % userid
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is None:
            conn.close()
            cursor.close()
            return ("Wrong user id!", False)
        elif result[0] == password:
            conn.close()
            cursor.close()
            return ("Login successful", True)
        else:
            conn.close()
            cursor.close()
            return ("Wrong password", False)

    def registration(self, userid, password):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=mysql_password, db='version2',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select * from customer where id = '%s'" % userid
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is not None:
            conn.close()
            cursor.close()
            return ("User ID exists, please enter a new username.", False)
        elif password != "" and userid != "":
            sql = "insert into customer(id, password) values" + "(" + userid + ", '" + password + "')"
            cursor.execute(sql)
            conn.commit()
            conn.close()
            cursor.close()
            return ("Registration successful", True)
        else:
            conn.close()
            cursor.close()
            return ("Empty id or password", False)
        

#Customer().registration("03", "1221")
