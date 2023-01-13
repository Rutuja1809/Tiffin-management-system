from cProfile import label
from tkinter import*
import tkinter
from PIL import ImageTk
from PIL import Image
from subprocess import call
import tkinter as tk
master=tkinter.Tk()
master.title("FRAGRANCE TIFFIN SERVICE")
master.geometry("1503x750+7+10") 
master.configure(bg="gray")
master.bg=ImageTk.PhotoImage(file="pics/veg-food-tiffin-services-.png")
master.bg_image=Label(master,image=master.bg).place(x=0,y=0,relwidth=1,relheight=1)

#frame1 = tk.LabelFrame(master,text="About Us",background='dark orange')
#frame1.place(height=60, width=230,x=400,y=600)
#root=Tk()
#Canvas=Canvas(master,width=20,height=20)
#Canvas.pack()
#Canvas.place(x=70,y=70)
#img=ImageTk.PhotoImage(Image.open("pics/CaptureTiffin2.jpg"))
#Canvas.create_image(10,10,anchor=NW,image=img)
#Canvas.place(relx=1, rely=1, anchor=CENTER)

def open2():
    call(['python' , 'adminLogin.py']) 
    master.destroy()
button1=tkinter.Button(master, text="Admin Login",fg="dark orange",bg="white", command=open2)
button1.place(x=1100,y=15)

def open():
    call(['python' , 'temp2.py'])
    master.destroy() 

button2=tkinter.Button(master, text="Customer Login",fg="dark orange",bg="white", command=open)
button2.place(x=1200,y=15)
label1=tkinter.Label(master,text="FRAGRANCE TIFFIN SERVICE",font=('impact',28),bg="white",fg="dark orange")
label1.place(x=20,y=20)

label2=tkinter.Label(master,text="About Us...",font=('impact',16),bg="white",fg="dark orange")
label2.place(x=20,y=100)
label3=tkinter.Label(master,text="We serve fresh and healthy",font=('impact',14),bg="white",fg="dark orange")
label3.place(x=20,y=140)
label4=tkinter.Label(master,text="home_made food...",font=('impact',14),bg="white",fg="dark orange")
label4.place(x=20,y=180)
#label5=tkinter.Label(master,text="who are living away from their homes...",font=('impact',14),bg="black",fg="dark orange")
#label5.place(x=20,y=210)

label6=tkinter.Label(master,text="Contact us...",font=('impact',16),bg="white",fg="dark orange")
label6.place(x=20,y=490)
label7=tkinter.Label(master,text="Rutuja Bhosale",font=('impact',14,'italic'),bg="white",fg="dark orange")
label7.place(x=20,y=530)
label8=tkinter.Label(master,text="Shraddha Murade",font=('impact',14,'italic'),bg="white",fg="dark orange")
label8.place(x=20,y=570)

label9=tkinter.Label(master,text="8767001747/7558686366",font=('impact',14),bg="white",fg="dark orange")
label9.place(x=20,y=610)
label10=tkinter.Label(master,text="Address- Talegaon",font=('impact',14),bg="white",fg="dark orange")
label10.place(x=20,y=650)


"""def open():
    call(['python' , 'registration.py']) 

button3=tkinter.Button(master, text="Wanna member", command=open)
button3.place(x=1022, y=20)
"""

master.mainloop()
