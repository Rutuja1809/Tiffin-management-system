import tkinter as tk
from my_connect import my_conn
from sqlalchemy.exc import SQLAlchemyError
my_w = tk.Tk()
my_w.geometry("1503x750+7+10")  # Size of the window 
my_w.title("www.plus2net.com")  # Adding a title
def my_p_table(): # 
    query="CREATE TABLE IF NOT EXISTS `plus2_products` ( \
      `p_id` int(3) NOT NULL AUTO_INCREMENT,\
    `p_name` varchar(100) NOT NULL,\
    `unit` varchar(20) NOT NULL,\
    `price` float(8,2) NOT NULL,\
    `p_cat` int(1) NOT NULL,\
    `available` int(1) NOT NULL DEFAULT '1',\
    PRIMARY KEY (`p_id`)\
    ) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=25 "
    try:
        rs=my_conn.execute(query) # run query to create table
    except SQLAlchemyError as e:
        error=str(e.__dict__['orig'])
        msg_display=error
        show_msg(msg_display,'error') # send error message 
    else:
        msg_display="Product Table is Created  "
        show_msg(msg_display,'normal')# success message 

def my_p_data():
    from product_data import product_data
    query="INSERT INTO `plus2_products`\
         (`p_id`, `p_name`, `unit`, `price`, `p_cat`, `available`) \
        VALUES (%s,%s,%s,%s,%s,%s)"
    try:
        rs=my_conn.execute(query,product_data)
    except SQLAlchemyError as e:
        error=str(e.__dict__['orig'])
        msg_display=error
        show_msg(msg_display,'error')
    else:
        msg_display="Number of rows added :" + str(rs.rowcount)
        show_msg(msg_display,'normal')
def delete_recs():
    #query="TRUNCATE table plus2_products"
    query="DELETE FROM  plus2_products"
    try:
        rs=my_conn.execute(query)
    except SQLAlchemyError as e:
        error=str(e.__dict__['orig'])
        msg_display=error
        show_msg(msg_display,'error')
    else:
        msg_display="Number of records removed :" + str(rs.rowcount)
        show_msg(msg_display,'normal')
def delete_table(): 
    query="DROP TABLE  plus2_products"
    try:
        rs=my_conn.execute(query)
    except SQLAlchemyError as e:
        error=str(e.__dict__['orig'])
        msg_display=error
        show_msg(msg_display,'error')
    else:
        msg_display="product table deleted " 
        show_msg(msg_display,'normal')
def show_msg(msg_display,type): # to show message to user 
    if(type=='normal'):
        l1.config(text=msg_display,fg='green')
    else:
        l1.config(text=msg_display,fg='red')
    my_w.after(3000,lambda:l1.config(text=''))
l_top=tk.Label(my_w,text='Restaurant Management : \n Installation of Tables ',
        fg='blue',font=('Times',24,'bold'))
l_top.grid(row=0,column=0,columnspan=4,padx=1,pady=20)
b1=tk.Button(my_w,text='Create Product table',command=my_p_table)
b1.grid(row=1,column=0,padx=1,pady=5)

b2=tk.Button(my_w,text='Add Data',command=my_p_data)
b2.grid(row=1,column=1,padx=1,pady=5)

b3=tk.Button(my_w,text='Delete records ',command=delete_recs)
b3.grid(row=1,column=2,padx=1,pady=5)

b4=tk.Button(my_w,text='Delete Tables ',command=delete_table)
b4.grid(row=1,column=3,padx=1,pady=5)

l1=tk.Label(my_w,font=('Times',12,'normal'))
l1.grid(row=3,column=0,padx=0,columnspan=4)

my_w.mainloop()  # Keep the window open