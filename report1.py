import tkinter as tk
from tkinter import ttk
from turtle import width
from tkcalendar import DateEntry 
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:214531@localhost/tifin")
my_w = tk.Tk()
my_w.geometry("900x650+225+87")  # Size of the window 
my_w.title("daily report") 
my_w.configure(bg="dark grey") # Adding a title
sel=tk.StringVar()
cal=DateEntry(my_w,selectmode='day',textvariable=sel)
cal.grid(row=0,column=0,padx=20,pady=30)
def my_upd(*args): # triggered when value of string varaible changes
    if(len(sel.get())>4):
        dt=cal.get_date() # get selected date object from calendar
        dt1=dt.strftime("%Y-%m-%d") #format for MySQL date column 
        dt2=dt.strftime("%d-%B-%Y") #format to display at label 
        l1.config(text=dt2) # display date at Label
        query="select * from plus2_sell WHERE bill_date=%s"
        r_set=my_conn.execute(query,dt1) # execute query with data
        for item in trv.get_children(): # delete all previous listings
            trv.delete(item)
        total=0 # to store total sale of the selected date
        for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
               values =(dt[1],dt[2],dt[3],dt[4],dt[5]))
            total=round(total+(dt[2]*dt[3]),2)
        l2.config(text="Total: " + str(total)) # show total value
l1=tk.Label(my_w,font=('Times',22,'bold'),fg='blue')
l1.grid(row=0,column=1)
trv = ttk.Treeview(my_w, selectmode ='browse')
  
trv.grid(row=1,column=1,padx=20,pady=10)
# number of columns
trv["columns"] = ("1", "2", "3","4","5")
trv['height']  =20
# Defining heading
trv['show'] = 'headings'
  
# width of columns and alignment 
trv.column("1", width = 30, anchor ='c')
trv.column("2", width = 80, anchor ='c')
trv.column("3", width = 80, anchor ='c')
trv.column("4", width = 80, anchor ='c')
trv.column("5", width = 80, anchor ='c')
  
# Headings  
# respective columns
trv.heading("1", text ="p_id")
trv.heading("2", text ="Price")
trv.heading("3", text ="Quantity")
trv.heading("4", text ="Bill_no")  
trv.heading("5", text ="Bill_date")
sel.trace('w',my_upd)

l2=tk.Label(my_w,font=('Times',22,'bold'),fg='red')
l2.grid(row=1,column=2,sticky='ne',pady=20)
#b1=tk.Button(my_w,text='monthly collection',font=('Times',22,'bold'),command=next)
#b1.grid(row=0,column=2)
my_w.mainloop()  # Keep the window open
