from tkinter import *
from tkinter import ttk
from turtle import bgcolor
from PIL import ImageTk
from PIL import Image
from tkinter import messagebox

root = Tk()
root.title("Feedback Form")
root.geometry("1503x750+7+10")
#root.configure(bg="black")
root.bg=ImageTk.PhotoImage(file="pics/feedback1.jpg")
root.bg_image=Label(root,image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)

#logo = PhotoImage(file='pics/tiffinWordForTiffinSystem.PNG').subsample(2, 2)
#logolabel = ttk.Label(image=logo)
#logolabel.grid(row=1, column=1, rowspan=2)

# def submit():
#     username = entry_name.get()
#     print(username)
myvar = StringVar()
var = StringVar()
# cmnt= StringVar()
namelabel = ttk.Label(text='Name')
namelabel.grid(padx=5, sticky='sw')
namelabel.place(x=300,y=110)

entry_name = ttk.Entry(width=18, font=('Arial', 14), textvariable=myvar)
entry_name.grid(row=2, column=2)
entry_name.place(x=300,y=130)

emaillabel = ttk.Label(text='Email')
emaillabel.grid(sticky='sw')
emaillabel.place(x=300,y=160)

entry_email = ttk.Entry(width=18, font=('Arial', 14), textvariable=var)
entry_email.place(x=300,y=180)

commentlabel = ttk.Label(text='Comment', font=('Arial', 10))
commentlabel.place(x=300,y=210)

textcomment = Text(width=50, height=10)
textcomment.grid(columnspan=2)
textcomment.place(x=300,y=230)


textcomment.config(wrap ='word')
# def clear():
#     textcomment.delete(1.0,'end')
def clear():
    global entry_name
    global entry_email
    global textcomment
    messagebox.showinfo(title='clear', message='Do you want to clear?')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


def submit():
    global entry_name
    global entry_email
    global textcomment
    print('Name:{}'.format(myvar.get()))
    print('Email:{}'.format(var.get()))
    print('Comment:{}'.format(textcomment.get(1.0, END)))
    messagebox.showinfo(title='Submit', message='Thank you for your Feedback, Your Comments Submited')
    entry_name.delete(0, END)
    entry_email.delete(0, END)
    textcomment.delete(1.0, END)


submitbutton = ttk.Button(text='Submit', command=submit)
submitbutton.place(x=420,y=400)
clearbutton = ttk.Button(text='Clear', command=clear).place(x=500,y=400)

mainloop()
