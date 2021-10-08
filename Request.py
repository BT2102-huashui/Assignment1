import pymysql
from Customers import DB_NAME, MY_SQL_PASSWORD, USERNAME
from Admins import Administrator

class Request(object):

    def submit_request(self, userid, itemid, ifinwarranty):
        conn = pymysql.connect(host='localhost', port=3306, user=USERNAME, password=MY_SQL_PASSWORD, db=DB_NAME, charset='utf8')
        cursor = conn.cursor()
        sql1 = """
        SELECT id
        FROM item
        WHERE customer_id = {}
        """
        sql1 = sql1.format(userid)
        cursor.execute(sql1)
        items = cursor.fetchone()
        if int(itemid) in items:
            if ifinwarranty:#purchase status lack
                sql2 = """
                INSERT request (date, request_status, service_status, customer_id, item_id, fee_amount) 
                VALUES(now(), 'Pro', 'Waiting', {}, {}, 0)
                """
                sql2 = sql2.format(userid, itemid)
                cursor.execute(sql2)
                conn.commit()
                conn.close()
                return print("Submmited")
            
            else:
                sql2 = """
                INSERT request (date, request_status, service_status, customer_id, item_id, fee_amount) 
                VALUES(now(), 'Sub and Wait', 'Waiting', {}, {}, {})
                """
                fee = calculateFee()#write a function to calculate
                sql2 = sql2.format(userid, itemid, fee)
                cursor.execute(sql2)
                conn.commit()
                conn.close()
                return print("Submmited and Waiting")
        else:
            return print("Cannot submit items for others")

    def calculateFee(self, itemid):
        conn = pymysql.connect(host='localhost', port=3306, user=USERNAME, password=MY_SQL_PASSWORD, db=DB_NAME, charset='utf8')
        cursor = conn.cursor()
        sql = "SELECT product_id FROM item WHERE id = {}".format(itemid)
        cursor.execute(sql2)
        productid = cursor.fetchone()[0]
        
Request().submit_request('1', '1001', True)

    # def payment(self,requestid):
    #     conn = pymysql.connect(host='localhost', port=3306, user=USERNAME, password=MY_SQL_PASSWORD, db=DB_NAME, charset='utf8')
    #     cursor = conn.cursor()
    #     sql = """
    #     UPDATE request
    #     SET request_status = 'Pro', Service_status = 'Waiting'
    #     WHERE id = {}
    #     """
    #     sql = sql.format(requestid)