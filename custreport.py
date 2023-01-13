from tkinter import *
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import ImageTk
from sqlalchemy import create_engine
my_conn1 = create_engine("mysql+mysqldb://root:214531@localhost/tifin")
root = tk.Tk()
root.geometry("900x650+225+87")
root.title("Payment Status")
root.configure(bg="dark grey")

ph1=tk.StringVar()

trv = ttk.Treeview(root, selectmode ='browse')
  
trv.place(x=10,y=300)
# number of columns
trv["columns"] = ("1", "2", "3","4","5","6")
trv['height']  =20
# Defining heading
trv['show'] = 'headings'
  
# width of columns and alignment 
trv.column("1", width = 50, anchor ='c')
trv.column("2", width = 50, anchor ='c')
trv.column("3", width = 80, anchor ='c')
trv.column("4", width = 80, anchor ='c')
trv.column("5", width = 80, anchor ='c')
trv.column("6", width = 60, anchor ='c')

  
# Headings  
# respective columns
trv.heading("1", text ="bill_no")
trv.heading("2", text ="bill_date")
trv.heading("3", text ="total")
trv.heading("4", text ="tax")  
trv.heading("5", text ="cust_e")
trv.heading("6", text ="status")
 # make the scrollbar fill the y axis of the Treeview widget


label1=Label(root,text="Name",font=('impact',32,'bold'),fg="black",bg='white')
label1.place(x=35, y=65)
label2=Label(root,text="select status",font=('impact',22,'bold'),fg="white",bg='black')
label2.place(x=50, y=170)

areaEntry = Entry(root, width=25, bd=5, font=('Arial', 15), textvariable = ph1)
areaEntry.place(x=150, y=65)


r1_v = tk.StringVar()
r1 = tk.Radiobutton(root, text='paid', variable=r1_v, value="paid")
r1.place(x=250, y=170) 
r2 = tk.Radiobutton(root, text='unpaid', variable=r1_v, value="unpaid")
r2.place(x=350, y=170)


def payment():
    query="select * from plus2_bill WHERE cust_e='"+ph1.get()+"' and status='"+r1_v.get()+"'"
    r_set=my_conn1.execute(query) # execute query with data
    for item in trv.get_children(): # delete all previous listings
        trv.delete(item)
    # to store total sale of the selected date
    for dt in r_set: 
        trv.insert("", 'end',iid=dt[0], text=dt[0],
        values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))

selectBtn = Button(root, text="Select", padx=35, pady=15, width=6,bd=1, font=('Arial', 15), bg="#EEEEEE", command=payment)
selectBtn.place(x=150, y=220)


root.mainloop()