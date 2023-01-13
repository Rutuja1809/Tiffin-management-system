from tkinter import *
from PIL import Image
from PIL import ImageTk

root=Tk()
root.geometry("1199x600+100+50")

root.title("Make Payment")

title=Label(text="Scan the image to make payment",font=("impact",25),fg="#d77337").place(x=90,y=30)
#title=Label(text="Login Here",font=("impact",25,"bold"),fg="#d77337").place(x=180,y=7)
root.mainloop()