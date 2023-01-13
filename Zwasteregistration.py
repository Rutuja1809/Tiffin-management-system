from tkinter import*
root = Tk()
root.geometry('1199x600+100+50')

root.title("Registration Form")
root.configure(bg="red")

def back():
    root.destroy()
    import login

label_0 = Label(root, text="Registration form",width=20,font=("bold", 20))
label_0.place(x=360,y=53)


label_1 = Label(root, text="FullName",width=20,font=("bold", 10))
label_1.place(x=360,y=130)

entry_1 = Entry(root)
entry_1.place(x=550,y=130)

label_2 = Label(root, text="Email",width=20,font=("bold", 10))
label_2.place(x=360,y=180)

entry_2 = Entry(root)
entry_2.place(x=550,y=180)

label_3 = Label(root, text="Gender",width=20,font=("bold", 10))
label_3.place(x=360,y=230)
var = IntVar()
Radiobutton(root, text="Male",padx = 5, variable=var, value=1).place(x=490,y=230)
Radiobutton(root, text="Female",padx = 20, variable=var, value=2).place(x=580,y=230)

label_4 = Label(root, text="address",width=20,font=("bold", 10))
label_4.place(x=360,y=280)


entry_2 = Entry(root)
entry_2.place(x=550,y=280)

Button(root, text='Submit',command=back,width=20,bg='brown',fg='white').place(x=470,y=380)
# it is use for display the registration form on the window
root.mainloop()
print("registration form  seccussfully created...")