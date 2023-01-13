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
                self.root.title("tiffin Management System") 
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
                definition.add_command(label="view menu", command=self.user_definition) 
                #definition.add_separator()
                
                menubar.add_cascade(label="Order", menu=definition)  
        
                purchase = Menu(menubar, tearoff=0)  
                purchase.add_command(label="Payment status" ,command=self.pay)  
                menubar.add_cascade(label="Payment", menu=purchase)  
        
                sales = Menu(menubar, tearoff=0)  
                sales.add_command(label="Feedback",command=self.feedbackk)  
                menubar.add_cascade(label="Feedback", menu=sales)  
                root.config(menu=menubar)
        def pay(self):
            call(['python' , 'custreport.py'])
            
        def feedbackk(self):
            call(['python' , 'feedback.py'])
            
        def user_definition(self):
            call(['python' , 'main_db.py'])
            
                
       
       

        
                
                

       
root = Tk()
obj = Wall(root)
root.mainloop()