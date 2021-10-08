import pymysql
import pymongo
import json
import pprint
from Customers import DB_NAME, MY_SQL_PASSWORD, USERNAME
from Mongodbdata import loadMongoDb


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

    def A_ID_Search(self, ID, f):
        client = pymongo.MongoClient()
        dbExist = client.list_database_names()

        if "inventory" not in dbExist:
            loadMongoDb()
            
        dic = {"ItemID":ID}
        dic.update(f)
        result = myItems.aggregate([{
        '$lookup':{
            'from': "products",
            'localField': "ProductID",
            'foreignField': "ProductID",
            'as': "combine"
            }
        },{'$match':
            dic},
        {'$project': { "_id":0, "Category":1, "Model":1, "Color":1, "PurchaseStatus":1, "CustomerID":1, "Color": 1, "Factory": 1,
                                       "PowerSupply" : 1, "ProductionYear" :1,
                       "Warranty":"$combine.Warranty (months)" , "Cost": "$combine.Cost ($)"}}
                
        ])
        resultlist = list(result)
        return resultlist

    def A_models_Search(self, m, f):
        client = pymongo.MongoClient()
        dbExist = client.list_database_names()

        if "inventory" not in dbExist:
            loadMongoDb()

        db = client["inventory"]
        myItems = db["items"]    
        dic = {"Model" : m}
        dic.update(f)
        newdic = dic.copy()
        dic["PurchaseStatus"]= "Sold"
        newdic["PurchaseStatus"]= "Unsold"
        
        listI = myItems.aggregate([{
        '$lookup':{
            'from': "products",
            'localField': "ProductID",
            'foreignField': "ProductID",
            'as': "combine"
            }
        },{'$match':
            newdic},
        {'$group': {"_id" : {"Category": "$Category", "Model":"$Model", "Warranty": "$combine.Warranty (months)","Cost": "$combine.Cost ($)",
                             "Price": "$combine.Price ($)"},
                    "Inventory": { "$sum": 1 }}},
        {'$project': {"_id":0, "Category":"$_id.Category", "Model":"$_id.Model", "Warranty": "$_id.Warranty","Cost": "$_id.Cost",
                             "Price": "$_id.Price", "Inventory_level":"$Inventory"}},
        {'$sort' : {"Category" :1}}
        ])

        resultListI = list(listI)

        
        result = myItems.aggregate([{
        '$lookup':{
            'from': "products",
            'localField': "ProductID",
            'foreignField': "ProductID",
            'as': "combine"
            }
        },{'$match':
            {"Category": c,"PurchaseStatus": "Sold"}},
        {'$group': {"_id" : {"Category": "$Category","Model":"$Model", "Warranty": "$combine.Warranty (months)","Cost": "$combine.Cost ($)",
                             "Price": "$combine.Price ($)"},
                    "SoldNumber": { "$sum": 1 }}},
        {'$project': {"_id":0, "Model":"$_id.Model", "Warranty": "$_id.Warranty","Cost": "$_id.Cost",
                             "Price": "$_id.Price", "SoldNumber":"$SoldNumber"}},
        {'$sort' : {"Model" :1}}
        ])
                
        resultlist = list(result)
        
        for i in range(len(resultlist)):
            resultlist[i]["Inventory_level"]= resultListI[i]["Inventory_level"]
        return resultlist

    def A_categories_Search(self, c, f):
        client = pymongo.MongoClient()
        dbExist = client.list_database_names()

        if "inventory" not in dbExist:
            loadMongoDb()

        db = client["inventory"]
        myItems = db["items"]
        dic = {"Category": c,}
        dic.update(f)
        newdic = dic.copy()
        dic["PurchaseStatus"]= "Sold"
        newdic["PurchaseStatus"]= "Unsold"
        
        listI = myItems.aggregate([{
        '$lookup':{
            'from': "products",
            'localField': "ProductID",
            'foreignField': "ProductID",
            'as': "combine"
            }
        },{'$match':
            newdic},
        {'$group': {"_id" : {"Category": "$Category", "Model":"$Model", "Warranty": "$combine.Warranty (months)","Cost": "$combine.Cost ($)",
                             "Price": "$combine.Price ($)"},
                    "Inventory": { "$sum": 1 }}},
        {'$project': {"_id":0, "Category": "$_id.Category", "Model":"$_id.Model", "Warranty": "$_id.Warranty","Cost": "$_id.Cost",
                             "Price": "$_id.Price", "Inventory_level":"$Inventory"}},
        {'$sort' : {"Model" :1}}
        ])

        resultListI = list(listI)

        
        result = myItems.aggregate([{
        '$lookup':{
            'from': "products",
            'localField': "ProductID",
            'foreignField': "ProductID",
            'as': "combine"
            }
        },{'$match':
            {"Category": c,"PurchaseStatus": "Sold"}},
        {'$group': {"_id" : {"Category": "$Category", "Model":"$Model", "Warranty": "$combine.Warranty (months)","Cost": "$combine.Cost ($)",
                             "Price": "$combine.Price ($)"},
                    "SoldNumber": { "$sum": 1 }}},
        {'$project': {"_id":0, "Category": "$_id.Category", "Model":"$_id.Model", "Warranty": "$_id.Warranty","Cost": "$_id.Cost",
                             "Price": "$_id.Price", "SoldNumber":"$SoldNumber"}},
        {'$sort' : {"Model" :1}}
        ])
                
        resultlist = list(result)
        
        for i in range(len(resultlist)):
            resultlist[i]["Inventory_level"]= resultListI[i]["Inventory_level"]
        
        return resultlist

print(Administrator().A_categories_Search("Lights",{}))

