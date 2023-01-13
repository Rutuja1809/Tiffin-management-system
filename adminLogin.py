from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
import mysqlx
import pymysql
import _mysql_connector
from subprocess import call
class Login:
   def back(self):
          call(['python' , 'home.py'])
          root.destroy
   def __init__(self,root):
      self.root=root
      self.root.title("Login and registration system")
      self.root.geometry("1503x750+7+10")
      self.root.resizable(False,False)
      self.loginform()
   def loginform(self):
      Frame_login=Frame(self.root,bg="white")
      Frame_login.place(x=0,y=0,height=750,width=1503)
      self.img=ImageTk.PhotoImage(file="images/img1.png")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,relwidth=1,relheight=1)
      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=320,y=130,height=450,width=350)
      label1=Label(frame_input,text="ADMIN Login",font=('impact',32,'bold'),fg="black",bg='white')
      label1.place(x=75,y=20)
      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label2.place(x=30,y=95)
      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      self.email_txt.place(x=30,y=145,width=270,height=35)
      label3=Label(frame_input,text="Password",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label3.place(x=30,y=195)
      self.password=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray')
      self.password.place(x=30,y=245,width=270,height=35)
      btn1=Button(frame_input,text="forgot password?",cursor='hand2',
      font=('calibri',10),bg='white',fg='black',bd=0)
      btn1.place(x=125,y=305)
      btn2=Button(frame_input,text="Login",command=self.login,cursor="hand2",
      font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn2.place(x=90,y=340)
     # btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      #btn3.place(x=110,y=390)
  
      btn3=Button(frame_input,text="BACK",command=self.back,cursor="hand2",
      font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn3.place(x=90,y=400)
      #btn3.after(3000, root.destroy)
      
   def login(self):
    
      if self.email_txt.get()=="" or self.password.get()=="":

         messagebox.showerror("Error","All fields are required",parent=self.root)

      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='214531',

                                database='tiffin')

            cur=con.cursor()

            cur.execute('select * from admin where name=%s and password=%s'

                        ,(self.email_txt.get(),self.password.get()))

            row=cur.fetchone()
            
            if row==None:

               messagebox.showerror('Error','Invalid Username And Password'

                                    ,parent=self.root)

               

               self.email_txt.focus()

            else:

               
               call(['python' , 'mainpage1.py'])
               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}'

                                 ,parent=self.root)

            

   
root=Tk() 
obj=Login(root)
root.mainloop()