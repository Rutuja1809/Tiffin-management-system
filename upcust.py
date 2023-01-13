#pip install PyMySQL
import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk

#connection for phpmyadmin
def connection():
    conn = pymysql.connect(
        host='localhost',
        user='root', 
        password='214531',
        db='tiffin',
    )
    return conn

def refreshTable():
    for data in my_tree.get_children():
        my_tree.delete(data)

    for array in read():
        my_tree.insert(parent='', index='end', iid=array, text="", values=(array), tag="orow")

    my_tree.tag_configure('orow', background='#EEEEEE', font=('Arial', 12))
    my_tree.grid(row=8, column=0, columnspan=5, rowspan=11, padx=10, pady=20)

root = Tk()
root.title("Customer Details")
root.geometry("1503x750+7+10")
my_tree = ttk.Treeview(root)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()
ph4 = tk.StringVar()
ph5 = tk.StringVar()

#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)
    if num ==4:
        ph4.set(word)
    if num ==5:
        ph5.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    cust_id = str(custidEntry.get())
    cust_name = str(fullnameEntry.get())
    Email_id = str(mailEntry.get())
    phone_no = str(phoneEntry.get())
    cust_address = str(addressEntry.get())

    if (cust_id == "" or cust_id == " ") or (cust_name == "" or cust_name == " ")  or (Email_id == "" or Email_id == " ") or (phone_no == "" or phone_no == " ") or ( cust_address== "" or cust_address == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO customer VALUES ('"+cust_id+"','"+cust_name+"','"+Email_id+"','"+phone_no+"','"+cust_address+"') ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "cust ID already exist")
            return

    refreshTable()
    

def reset():
    decision = messagebox.askquestion("Warning!!", "Delete all data?")
    if decision != "yes":
        return 
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("delete FROM customer")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def delete():
    decision = messagebox.askquestion("Warning!!", "Delete the selected data?")
    if decision != "yes":
        return 
    else:
        selected_item = my_tree.selection()[0]
        deleteData = str(my_tree.item(selected_item)['values'][0])
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("delete FROM customer WHERE cust_id='"+str(deleteData)+"'")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Sorry an error occured")
            return

        refreshTable()

def select():
    try:
        selected_item = my_tree.selection()[0]
        cust_id = str(my_tree.item(selected_item)['values'][0])
        cust_name = str(my_tree.item(selected_item)['values'][1])
        Email_id = str(my_tree.item(selected_item)['values'][2])
        phone_no = str(my_tree.item(selected_item)['values'][3])
        cust_address = str(my_tree.item(selected_item)['values'][4])

        setph(cust_id,1)
        setph(cust_name,2)
        setph(Email_id,3)
        setph(phone_no,4)
        setph(cust_address,5)
    except:
        messagebox.showinfo("Error", "Please select a data row")

def search():
    cust_id = str(custidEntry.get())
    cust_name = str(fullnameEntry.get())
    Email_id = str(mailEntry.get())
    phone_no = str(phoneEntry.get())
    cust_address = str(addressEntry.get())

    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM customer WHERE cust_id='"+
    cust_id+"' or cust_name='"+
    cust_name+"' or Email_id='"+
    Email_id+"' or phone_no='"+
    phone_no+"' or cust_address='"+
    cust_address+"' ")
    
    try:
        result = cursor.fetchall()

        for num in range(0,5):
            setph(result[0][num],(num+1))

        conn.commit()
        conn.close()
    except:
        messagebox.showinfo("Error", "No data found")

def update():
    selectedcust_id = ""

    try:
        selected_item = my_tree.selection()[0]
        selectedcust_id = str(my_tree.item(selected_item)['values'][0])
    except:
        messagebox.showinfo("Error", "Please select a data row")

    cust_id = str(custidEntry.get())
    cust_name = str(fullnameEntry.get())
    Email_id = str(mailEntry.get())
    phone_no = str(phoneEntry.get())
    cust_address = str(addressEntry.get())

    if (cust_id == "" or cust_id == " ") or (cust_name == "" or cust_name == " ") or (cust_address == "" or cust_address == " ") or (Email_id == "" or Email_id == " ") or (phone_no == "" or phone_no == " "):
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE customer SET cust_id='"+
            cust_id+"', cust_name='"+
            cust_name+"', cust_address='"+
            cust_address+"', Email_id='"+
            Email_id+"', phone_no='"+
            phone_no+"' WHERE cust_id='"+
            selectedcust_id+"' ")
            conn.commit()
            conn.close()
        except:
            messagebox.showinfo("Error", "Stud ID already exist")
            return

    refreshTable()

label = Label(root, text="Customer Details", font=('Arial Bold', 30))
label.grid(row=0, column=0, columnspan=8, rowspan=2, padx=50, pady=40)

custidLabel = Label(root, text="Cust ID", font=('Arial', 15))
fnameLabel = Label(root, text=" FullName", font=('Arial', 15))
mailLabel = Label(root, text="Email Id", font=('Arial', 15))
phoneLabel = Label(root, text="Phone", font=('Arial', 15))
addressLabel = Label(root, text="Address", font=('Arial', 15))

custidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)
fnameLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
mailLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
phoneLabel.grid(row=6, column=0, columnspan=1, padx=50, pady=5)
addressLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

custidEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)
fullnameEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
mailEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
phoneEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph4)
addressEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

custidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
fullnameEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
mailEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)
phoneEntry.grid(row=6, column=1, columnspan=4, padx=5, pady=0)
addressEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Add", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="orange", command=add)
selectBtn = Button(
    root, text="Select", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="green", command=select)

deleteBtn = Button(
    root, text="Delete", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="orange", command=delete)
searchBtn = Button(
    root, text="Search", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="green", command=search)
resetBtn = Button(
    root, text="Reset", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="orange", command=reset)
updateBtn = Button(
    root, text="update", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="green", command=update)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)
selectBtn.grid(row=5, column=5, columnspan=1, rowspan=2)
deleteBtn.grid(row=7, column=5, columnspan=1, rowspan=2)
searchBtn.grid(row=9, column=5, columnspan=1, rowspan=2)
resetBtn.grid(row=11, column=5, columnspan=1, rowspan=2)
updateBtn.grid(row=13, column=5, columnspan=1, rowspan=2)

style = ttk.Style()
style.configure("Treeview.Heading", font=('Arial Bold', 15))

my_tree['columns'] = ("CUST ID","Fullname","Email Id","Phone","Address")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("CUST ID", anchor=W, width=170)
my_tree.column("Fullname", anchor=W, width=150)
my_tree.column("Email Id", anchor=W, width=150)
my_tree.column("Phone", anchor=W, width=165)
my_tree.column("Address", anchor=W, width=150)

my_tree.heading("CUST ID", text="Cust ID", anchor=W)
my_tree.heading("Fullname", text="Fullname", anchor=W)
my_tree.heading("Email Id", text="Email Id", anchor=W)
my_tree.heading("Phone", text="Phone", anchor=W)
my_tree.heading("Address", text="Address", anchor=W)

refreshTable()

root.mainloop()