import pymysql
mysql_password = "ur password"

class Administrator(object):
    def login(self, userid, password):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=mysql_password, db='version2',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select password from administrator where id = '%s'" % userid
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

    def registration(self, userid, password, gender):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=mysql_password, db='version2',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select * from administrator where id = '%s'" % userid
        cursor.execute(sql)
        result = cursor.fetchone()
        if result is not None:
            conn.close()
            cursor.close()
            return ("User ID exists, please enter a new username.", False)
        elif password != "" and userid != "":
            sql = "insert into administrator(id, password, gender) values" + "('" + userid + "', '" + password + "', '" + gender + "')"
            cursor.execute(sql)
            conn.commit()
            conn.close()
            cursor.close()
            return ("Registration successful", True)
        else:
            conn.close()
            cursor.close()
            return ("Empty id or password", False)
    
    def product_manage(self):
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=mysql_password, db='version2',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select product_id, count(purchase_status = 'Yes' or null), count(purchase_status = 'No' or null)  \
              from item group by product_id order by product_id"
        cursor.execute(sql)
        results = cursor.fetchall()
        num_rows = len(results)
        values = ()
        pointer = 0
        for i in range(1, 8):
            if pointer == num_rows:
                values = values + ((i, 0, 0), )
            elif i == 1:
                if results[0][0] == 1:
                    values = (results[0], )
                    pointer = pointer + 1
                else:
                    values = ((1, 0, 0), )
            else:
                if results[pointer][0] == i:
                    values = values + (results[pointer],)
                    pointer = pointer + 1
                else:
                    values = values + ((i, 0, 0),)
        return values
#Administrator().product_manage()

