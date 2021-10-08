import os
import sys
sys.path.append(os.getcwd())
import pymysql
import pymongo
from dotenv import load_dotenv
from Mongodbdata import loadMongoDb
load_dotenv()
MY_SQL_PASSWORD = os.getenv('MY_SQL_PASSWORD')
SQL_FILE = os.getenv('SQL_FILE')
DB_NAME = os.getenv('DB_NAME')
USERNAME = os.getenv('USERNAME')

class Customer:
    def __init__(self) -> None:
        super().__init__()
        
    def login(self, userid, password):
        conn = pymysql.connect(host='localhost', port=3306, user=USERNAME, password=MY_SQL_PASSWORD, db=DB_NAME,
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

    def registration(self, userid, password, name, gender, number, address, email):
        conn = pymysql.connect(host='localhost', port=3306, user=USERNAME, password=MY_SQL_PASSWORD, db=DB_NAME,
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
            sql = """
            INSERT INTO customer(id, password, name, gender, phone_number, address, email_address) 
            VALUES({}, '{}', '{}', '{}', '{}', '{}', '{}')
            """
            sql = sql.format(userid, password, name, gender, number, address, email)
            cursor.execute(sql)
            conn.commit()
            conn.close()
            cursor.close()
            return ("Registration successful", True)
        else:
            conn.close()
            cursor.close()
            return ("Empty id or password", False)

    def C_categories_Search(self, c, f, n):
        client = pymongo.MongoClient()
        dbExist = client.list_database_names()

        if "inventory" not in dbExist:
            loadMongodb()
        db = client["inventory"]
        myItems = db["items"]
        dic = {"Category": c, "CustomerID": n}
        dic.update(f)
        listI = myItems.aggregate([{
        '$lookup':{
            'from': "products",
            'localField': "ProductID",
            'foreignField': "ProductID",
            'as': "combine"
            }
        },{'$match':
            dic},
        {'$group': {"_id" : {"Category": "$Category", "Model":"$Model", "Warranty": "$combine.Warranty (months)","Cost": "$combine.Cost ($)",
                             "Price": "$combine.Price ($)"},
                    "Inventory": { "$sum": 1 }}},
        {'$project': {"_id":0, "Category":"$_id.Category", "Model":"$_id.Model", "Warranty": "$_id.Warranty","Cost": "$_id.Cost",
                             "Price": "$_id.Price", "Inventory_level":"$Inventory"}},
        {'$sort' : {"Category" :1}}
        ])

        resultListI = list(listI)
        return resultListI
    
    def C_models_Search(self, m, f, n):
        client = pymongo.MongoClient()
        dbExist = client.list_database_names()

        if "inventory" not in dbExist:
            loadMongodb()
        db = client["inventory"]
        myItems = db["items"]
        dic = {"Model" : m, "CustomerID": n}
        dic.update(f)
        listI = myItems.aggregate([{
        '$lookup':{
            'from': "products",
            'localField': "ProductID",
            'foreignField': "ProductID",
            'as': "combine"
            }
        },{'$match':
            dic},
        {'$group': {"_id" : {"Category": "$Category", "Model":"$Model", "Warranty": "$combine.Warranty (months)","Cost": "$combine.Cost ($)",
                             "Price": "$combine.Price ($)"},
                    "Inventory": { "$sum": 1 }}},
        {'$project': {"_id":0, "Category":"$_id.Category", "Model":"$_id.Model", "Warranty": "$_id.Warranty","Cost": "$_id.Cost",
                             "Price": "$_id.Price", "Inventory_level":"$Inventory"}},
        {'$sort' : {"Category" :1}}
        ])

        resultListI = list(listI)
        return resultListI

        

#Customer().registration("03", "1221")
#print(Customer().C_categories_Search("Lights", {}, "12"))
