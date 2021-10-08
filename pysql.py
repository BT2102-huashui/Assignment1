# -*- coding: utf-8 -*-
"""
Created on Sat Sep 25 12:58:58 2021

@author: 徐骁翔
"""


from pymysql import *

#%%
def create():
    cursor1=conn.cursor()
    
    #cursor1.execute("DROP SCHEMA version2")

    #create database
    cursor1.execute('CREATE DATABASE IF NOT EXISTS version2')
    #create table administrator
    cursor1.execute("""CREATE TABLE IF NOT EXISTS version2.administrator (
            	id INT PRIMARY KEY NOT NULL,
                name VARCHAR(50) NOT NULL,
                gender ENUM('Female', 'Male') NOT NULL,
                phone_number VARCHAR(20) NOT NULL,
                password VARCHAR(50) NOT NULL
            )""")
    #create table customer
    cursor1.execute("""CREATE TABLE IF NOT EXISTS version2.customer (
            	id INT PRIMARY KEY NOT NULL,
                password VARCHAR(50) NOT NULL,
                name VARCHAR(50) NOT NULL,
                gender ENUM('Female', 'Male') NOT NULL,
                phone_number VARCHAR(20) NOT NULL,
                address VARCHAR(100) NOT NULL,
                email_address VARCHAR(50) NOT NULL
            )""")
    #create table item
    cursor1.execute("""CREATE TABLE IF NOT EXISTS version2.item (
            	id INT PRIMARY KEY NOT NULL,
                category ENUM('Lights', 'Locks') NOT NULL,
                model ENUM('Light1', 'Light2', 'SmartHome1', 'Safe1', 'Safe2', 'Safe3') NOT NULL,
                purchase_status ENUM('Yes', 'No') NOT NULL,
                purchase_date DATE NOT NULL,
                customer_id INT NOT NULL,
                admin_id INT NOT NULL,
                FOREIGN KEY (customer_id) REFERENCES version2.customer(id),
                FOREIGN KEY (admin_id) REFERENCES version2.administrator(id)
            )""")
    #create table request
    cursor1.execute("""CREATE TABLE IF NOT EXISTS version2.request (
            	id INT PRIMARY KEY NOT NULL,
                date DATE NOT NULL,
                request_status ENUM('Sub', 'Sub and Wait', 'Pro', 'Appr', 'Can', 'Com') NOT NULL,
                service_status ENUM('Waiting', 'Progress', 'Completed') NOT NULL,
                customer_id INT NOT NULL,
                admin_id INT NOT NULL,
                item_id INT NOT NULL,
            	fee_amount float(20,2),
                payment_date DATE,
                create_DATE DATE,
                FOREIGN KEY (customer_id) REFERENCES version2.customer(id),
                FOREIGN KEY (admin_id) REFERENCES version2.administrator(id),
                FOREIGN KEY (item_id) REFERENCES version2.item(id)
            )""")

    cursor1.close()


#%%
def call_num_of_items_sold():
    cursor2=conn.cursor()
    
    try:
       cursor2.execute("""select category,model,sum(id) as num_of_items_sold
                        from version2.item
                        where purchase_status='Yes'
                        group by category,model
                        order by category,model""")
       results = cursor2.fetchall()
       print('{:<10}{:^10}{:>10}'.format('category','model','num_of_items_sold'))
       for row in results:
           print('{:<10}{:^10}{:>10}'.format(row[0],row[1],row[2]))
    except:
       print("Error: unable to fecth data")
    
    cursor2.close()
    function()
       
#%% 
def call_items_under_service():
    cursor3=conn.cursor()
    
    try:
       cursor3.execute("""select item_id,service_status,category,model
                        from version2.request
                        where service_status='Waiting' or service_status='Progress'
                        order by service_status,item_id""")
       results = cursor3.fetchall()       
       print('{:<12}{:<12}{:<12}{:<12}'.format('service_status','item_id','category','model'))
       for row in results:
           print('{:<12}{:<12}{:<12}{:<12}'.format(row[0],row[1],row[2],row[3]))
    except:
       print("Error: unable to fecth data")
    
    cursor3.close()
    function()


#%%
def call_customers_with_fee_unpaid():
    cursor4=conn.cursor()
    
    try:
       cursor4.execute("""select r.customer_id,r.fee_amount,c.name,c.phone_number,c.address,c.email_address
                        from version2.request r,version2.customer c
                        where r.customer_id=c.id and r.request_status='Sub and Wait'
                        order by customer_id,name""")
       results = cursor4.fetchall()
       print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format('customer_id','fee_amount','name','phone_number','address','email_address'))
       for row in results:
           print('{:<10}{:<10}{:<10}{:<10}{:<10}{:<10}'.format(row[0],row[1],row[2],row[3],row[4],row[5]))
    except:
       print("Error: unable to fecth data")
    
    cursor4.close()
    function()

#%%  
def function():
    call=input("""press 1 to call num_of_items_sold\npress 2 to call items_under_service\npress 3 to call customers_with_fee_unpaid\npress 0 to exit\n""")
    if eval(call)==1:
        call_num_of_items_sold()
    elif eval(call)==2:
        call_items_under_service()
    elif eval(call)==3:
        call_customers_with_fee_unpaid()
    elif eval(call)==0:
        break
    else:
        if eval(input('input error, please try again, press 0 to exit\n'))==0:
            break
        else:
            function()
        
#%%       
if __name__=='__main__':
    conn=connect(host='localhost',port=3306,user='root',password='147147',database='new_schema',charset='utf8')
    create()
    conn.close()
else:
    function()
        
