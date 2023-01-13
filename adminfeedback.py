import pymysql
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
root = Tk()
root.title("Feedback Details")
root.geometry("900x650+225+87")
root.configure(bg="dark grey")
my_tree = ttk.Treeview(root)
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



def read():
    conn = connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM feedback")
    results = cursor.fetchall()
    conn.commit()
    conn.close()
    return results


my_tree['columns'] = ("Email_id","comment")

my_tree.column("#0", width=0, stretch=NO)
my_tree.column("Email_id", anchor=W, width=170)
my_tree.column("comment", anchor=W, width=250)

my_tree.heading("Email_id", text="Customer", anchor=W)
my_tree.heading("comment", text="Comment", anchor=W)

refreshTable()

root.mainloop()