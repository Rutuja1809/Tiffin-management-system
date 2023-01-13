import random
from datetime import timedelta,date
from my_connect import my_conn # database connection. 
#query="TRUNCATE plus2_sell"# remove all data from table 
#my_conn.execute(query) # remove all data from table 
#query="TRUNCATE plus2_bill"# remove all data from table 
#my_conn.execute(query)# remove all data from table 

d=date.today() # todays date 
def my_insert(td):
    dt=d+ timedelta(days=-td) # date object created 
    dt=dt.strftime('%Y-%m-%d') # date string 
    dl=[] # list to store data
    total=0 
    no_of_sell=random.randint(3,6) # number of sell in a day
    for i in range(no_of_sell):
        dl_item=[]
        p_id=random.randint(1,8)
        quantity=random.randint(1,5)
        query="select price FROM plus2_products WHERE p_id = %s"
        my_cursor=my_conn.execute(query,p_id)
        my_result = my_cursor.fetchone()
        #print(my_result[0])
        dl_item.append(p_id)
        dl_item.append(my_result[0])
        dl_item.append(quantity)
        price=my_result[0]*quantity
        total=round(total+price,2)
        dl.append(dl_item)
    tax=round(0.1*total,2)
    
    query="insert INTO  plus2_bill (Total,tax,`bill_date`) \
                  VALUES (%s,%s,%s)"
    data=[total,tax,dt]
    id=my_conn.execute(query,data)
    bill_no=id.lastrowid
    for i in dl:
        i.insert(3,bill_no)
        i.insert(4,dt)
    query="insert INTO plus2_sell(p_id,price,quantity,bill_no,bill_date)\
                  VALUES(%s,%s,%s,%s,%s)"
    id=my_conn.execute(query,dl)
for i in range(0,31): # increase the range to store more days
    my_insert(1)
