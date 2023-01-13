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


root = Tk()
root.title("Customer Details")
root.geometry("1503x750+7+10")
#my_tree = ttk.Treeview(root)

#placeholders for entry
ph1 = tk.StringVar()
ph2 = tk.StringVar()
ph3 = tk.StringVar()


#placeholder set value function
def setph(word,num):
    if num ==1:
        ph1.set(word)
    if num ==2:
        ph2.set(word)
    if num ==3:
        ph3.set(word)

def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results

def add():
    #cust_id = str(custidEntry.get())
    
    Email_id = str(mailEntry.get())
    comment = str(commentEntry.get())
    #cust_address = str(addressEntry.get())

    if (Email_id == "" or Email_id == " ") or (comment == "" or comment == " ") :
        messagebox.showinfo("Error", "Please fill up the blank entry")
        return
    else:
        try:
            conn = connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO feedback VALUES ('"+Email_id+"','"+comment+"') ")
            conn.commit()
            conn.close()
            messagebox.showinfo("Error", "Thank you for feedback...!!!!")
        except:
            messagebox.showinfo("Error", "you can submit one comment only")
            return
        

    
mailLabel = Label(root, text="Email Id", font=('Arial', 15))
commentLabel = Label(root, text="comment", font=('Arial', 15))
#addressLabel = Label(root, text="Address", font=('Arial', 15))

#custidLabel.grid(row=3, column=0, columnspan=1, padx=50, pady=5)

mailLabel.grid(row=4, column=0, columnspan=1, padx=50, pady=5)
commentLabel.grid(row=5, column=0, columnspan=1, padx=50, pady=5)
#addressLabel.grid(row=7, column=0, columnspan=1, padx=50, pady=5)

#custidEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph1)

mailEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph2)
commentEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph3)
#addressEntry = Entry(root, width=55, bd=5, font=('Arial', 15), textvariable = ph5)

#custidEntry.grid(row=3, column=1, columnspan=4, padx=5, pady=0)
mailEntry.grid(row=4, column=1, columnspan=4, padx=5, pady=0)
commentEntry.grid(row=5, column=1, columnspan=4, padx=5, pady=0)


#addressEntry.grid(row=7, column=1, columnspan=4, padx=5, pady=0)

addBtn = Button(
    root, text="Submit", padx=65, pady=25, width=10,
    bd=5, font=('Arial', 15), bg="orange", command=add)

addBtn.grid(row=3, column=5, columnspan=1, rowspan=2)

root.mainloop()