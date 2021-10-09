import pymysql
import pymongo
import json
import pprint
from Customers import DB_NAME, MY_SQL_PASSWORD, USERNAME
from Mongodbdata import loadMongoDb
from Search import searchfordetail


class Administrator(object):
        
    def login(self, userid, password):
        conn = pymysql.connect(host='localhost', port=3306, user=USERNAME, password=MY_SQL_PASSWORD, db=DB_NAME,
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

    def registration(self, userid, password, name, gender, number):
        conn = pymysql.connect(host='localhost', port=3306, user=USERNAME, password=MY_SQL_PASSWORD, db=DB_NAME,
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
            sql = """
            INSERT INTO administrator(id, password, name, gender, phone_number) values({}, '{}', '{}', '{}', '{}')
            """
            sql = sql.format(userid, password, name, gender, number)
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
        conn = pymysql.connect(host='localhost', port=3306, user='root', password=MY_SQL_PASSWORD, db='bt2102',
                               charset='utf8')
        cursor = conn.cursor()
        sql = "select product_id, count(purchase_status = 'Sold' or null), count(purchase_status = 'Unsold' or null)  \
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

    def A_ID_Search(self, ID):
        return searchfordetail(ID, {},False, False, True)

    def A_models_Search(self, m, f):
        return searchfordetail(m, f, False, False, False)

    def A_categories_Search(self, c, f):
        return searchfordetail(c, f, True, False, False)

    
#print(Administrator().A_ID_Search("1001"))

