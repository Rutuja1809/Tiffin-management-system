import tkinter as tk  
from tkinter import ttk  
from tkinter import Menu  

win = tk.Tk()  
win.title("Customer Mainframe") 
win.geometry("1199x600+100+50")
#Exit action  
def back():
   win.destroy()
   #import myorder
def _quit():  
   win.quit()  
   win.destroy()  
   exit()  
#Create Menu Bar  
menuBar=Menu(win)  
win.config(menu=menuBar)  
#customer module  
customerMenu= Menu(menuBar, tearoff=0)  
customerMenu.add_command(label="New",command=back)  
customerMenu.add_separator()  
customerMenu.add_command(label="Exit", command=_quit)  
menuBar.add_cascade(label="customer", menu=customerMenu)  
#myorder module  
myorderMenu= Menu(menuBar)  
myorderMenu.add_command(label="About", command=back)  
menuBar.add_cascade(label="Myorder", menu=myorderMenu,font=(45))  
#payment module  
paymentMenu= Menu(menuBar, tearoff=0)  
paymentMenu.add_command(label="About")  
menuBar.add_cascade(label="payment", menu=paymentMenu)  
#Calling Main()  
win.mainloop()