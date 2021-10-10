import os
import sys
sys.path.append(os.getcwd())
import pymysql
import json
from dotenv import load_dotenv
load_dotenv()

MY_SQL_PASSWORD = os.getenv('MY_SQL_PASSWORD')
SQL_FILE = os.getenv('SQL_FILE')
DB_NAME = os.getenv('DB_NAME')
USERNAME = 'root'

def checkSQL(filename):
    conn = pymysql.connect(host='localhost', port=3306, user=USERNAME, password=MY_SQL_PASSWORD, charset='utf8')
    cursor = conn.cursor()
    fd = open(filename, 'r')
    sqlFile = fd.read()
    fd.close()
    sqlCommands = sqlFile.split(';')

    for command in sqlCommands:
        if command.strip() != '':
            cursor.execute(command)
            conn.commit()
    #insert items
    json_items_data = open('items.json').read()
    json_items = json.loads(json_items_data)
    for item in json_items:
        itemID = item.get('ItemID')
        category = item.get('Category')
        purchasestatus = item.get('PurchaseStatus')
        model = item.get('Model')
        cursor.execute('INSERT INTO bt2102.item(id, category, purchase_status, model) value(%s, %s, %s, %s)', (itemID, category, purchasestatus, model))
    conn.commit()

    json_products_data = open('products.json').read()
    json_products = json.loads(json_products_data)

    for product in json_products:
        productID = product.get('ProductID')
        product_category = product.get('Category')
        product_model = product.get('Model')
        product_price = product.get('Price ($)')
        product_warranty = product.get('Warranty (months)')
        print(product_warranty)
        cursor.execute('insert into bt2102.product(id, category, model, price, warranty) value(%s, %s, %s, %s, %s)', (productID, product_category, product_model, product_price, product_warranty))
    conn.commit()
    conn.close()


if __name__ == "__main__":
    #checkSQL(SQL_FILE)
    from MainPages import Main_Page
    Main_Page().mainloop()