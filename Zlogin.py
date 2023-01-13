import tkinter
from tkinter import *
from PIL import Image
from PIL import ImageTk

root=Tk()
root.geometry("1503x750+7+10")

root.title("Login Page")
root.bg=ImageTk.PhotoImage(file="pics/06032017_dabba01.jpg")
root.bg_image=Label(image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)
root.configure(bg="black")
def back():
    back.destroy()
    #import mainpage

title=Label(text="Login Here",font=("impact",25,"bold"),fg="#d77337").place(x=600,y=40)
#desc=Label(text="Login To Fragrance Tiffin Service",font=("Goudy old style",13,"bold"),fg="black",bg="#d77337").place(x=90,y=100)

lbl_user=Label(text="Registered Name",font=("Goudy old style",15,"bold"),fg="white",bg="green").place(x=600,y=210)
root.txt_user=Entry(font=("times new roman",15),bg="white")
root.txt_user.place(x=600,y=240,width=350,height=35)

lbl_pass=Label(text="Registered Password",font=("Goudy old style",15,"bold"),fg="white",bg="green").place(x=600,y=280)
root.txt_pass=Entry(font=("times new roman",15),bg="white",fg="black")
root.txt_pass.place(x=600,y=310,width=350,height=35)

forget_btn=Button(text="Forgot password",bg="green",fg="white",bd=0,font=("times new roman",12)).place(x=600,y=350)
login_btn=Button(root,command=back,text="Login",fg="white",bg="#d77337",font=("times new roman",17)).place(x=600,y=390,width=100,height=28)

root.mainloop()