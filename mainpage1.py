from tkinter import*
import pymysql
from PIL import Image
from PIL import ImageTk
from tkinter import messagebox , Menu 
#from subprocess import call
from subprocess import call
class Wall:
        def __init__(self, root):
                self.root = root
                self.root.title("Tiffin Management System")
                #self.root.resizable(False,False)
                self.root.geometry("1503x750+7+10")
                self.root.bg=ImageTk.PhotoImage(file="pics/mainpage2.jpg")
                self.root.bg_image=Label(image=root.bg).place(x=0,y=0,relwidth=1,relheight=1)
# Creating Menu bar for Applicaiton

                #Frame_login = Frame(self.root, bg='white',borderwidth = 3, relief = "sunken")
                #Frame_login.place(x=10,y=5, height =100 , width =620)
                #login_Button = Button(Frame_login,text = "Login",command=self.user_definition,cursor="hand2", font=("Times New Roman" , 12)).place(x=2,y=10, height =40 , width =125)
        

                menubar = Menu(root)  
                file = Menu(menubar, tearoff=0)  
                file.add_command(label="Exit", command=root.quit)  
                menubar.add_cascade(label="Logout", menu=file)  
                
                definition = Menu(menubar, tearoff=0)  
                menubar.add_cascade(label="Report", menu=definition)  
                definition.add_command(label="DAILY", command=self.u_definition) 
                definition.add_separator()
                definition.add_command(label="Monthly Data", command=self.c_definition)  
                #definition.add_separator()
                  
                
        
                purchase = Menu(menubar, tearoff=0)  
                purchase.add_command(label="EDIT" ,command=self.pay)  
                menubar.add_cascade(label="Menu", menu=purchase)  
        
                  
                 
                menubar.add_cascade(label="Feedback",command=self.feedbackk)  
                root.config(menu=menubar)

                  
                menubar.add_cascade(label="Customer detail",command=self.cust)  
                root.config(menu=menubar)

                  
                menubar.add_cascade(label="payment",command=self.payment)  
                root.config(menu=menubar)
        def cust(self):
            
            call(['python' , 'upcust.py'])
        def payment(self):
            call(['python' , 'adminpay.py'])
        def pay(self):
            call(['python' , 'menu_edit.py'])
        def feedbackk(self):
            call(['python' , 'adminfeedback.py'])
        def u_definition(self):
            call(['python' , 'report1.py'])
        def c_definition(self):
            call(['python' , 'temp3.py'])

        
                
                

       
root = Tk()
obj = Wall(root)
root.mainloop()