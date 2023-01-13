from tkinter import*
root=Tk()
root.geometry("1199x600+100+50")
root.title("Payment")
def back():
    import Zpayment2

title=Label(text="Enter details to make payment",font=("impact",25),fg="#d77337").place(x=90,y=30)
title=Label(text="Full Name",font=("impact",15)).place(x=110,y=120)
txt_pass=Entry(font=("times new roman",15),bg="lightgray")
txt_pass.place(x=200,y=120,width=350,height=35)

title=Label(text="Email ",font=("impact",15)).place(x=130,y=170)
txt_pass=Entry(font=("times new roman",15),bg="lightgray")
txt_pass.place(x=200,y=170,width=350,height=35)

procced_btn=Button(root,command=back,text="Procced",fg="white",bg="#d77337",font=("times new roman",20)).place(x=535,y=470,width=180,height=40)

root.mainloop()