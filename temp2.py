import email
from msilib.schema import AppSearch
from tkinter import*
import tkinter as tk
import tkinter as ttk
from turtle import width
from PIL import ImageTk
from tkinter import messagebox
import mysqlx
import pymysql
import _mysql_connector
from sqlalchemy import create_engine
my_conn = create_engine("mysql+mysqldb://root:214531@localhost/tiffin")
from sqlalchemy import create_engine
my_conn1 = create_engine("mysql+mysqldb://root:214531@localhost/tifin")
from subprocess import call

class Login: 
   def back(self):
          
          import mainpage1
          
   def __init__(self,root):
      self.root=root
      self.root.title("Login and registration system")
      self.root.geometry("1350x700+60+50")
      self.root.resizable(False,False)
      self.loginform()
      
   def loginform(self):
      Frame_login=Frame(self.root,bg="red")
      Frame_login.place(x=0,y=0,height=700,width=1366)
      self.img=ImageTk.PhotoImage(file="images/img2.JPG")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
      frame_input=Frame(self.root,bg='white')
      frame_input.place(x=320,y=130,height=450,width=350)
      label1=Label(frame_input,text="Login",font=('impact',32,'bold'),fg="black",bg='white')
      label1.place(x=75,y=20)
      label2=Label(frame_input,text="Username",font=("Goudy old style",20,"bold"),fg='orangered',bg='white')
      label2.place(x=30,y=95)
      e1=tk.StringVar() 
      self.email_txt=Entry(frame_input,font=("times new roman",15,"bold"),bg='lightgray',textvariable=e1)
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
      #btn3=Button(frame_input,command=self.Register,text="Not Registered?register",cursor="hand2",font=("calibri",10),bg='white',fg="black",bd=0)
      #btn3.place(x=110,y=390)
      btn3=Button(frame_input,text="REGISTER",command=self.Register,cursor="hand2",
      font=("times new roman",15),fg="white",bg="orangered",bd=0,width=15,height=1)
      btn3.place(x=90,y=400)
      btn3.after(3000)
       
   def login(self):
    
      if self.email_txt.get()=="" or self.password.get()=="":

         messagebox.showerror("Error","All fields are required",parent=self.root)

      else:

         try:

            con=pymysql.connect(host='localhost',user='root',password='214531',

                                database='tiffin')

            cur=con.cursor()

            cur.execute('select * from register where username=%s and password=%s'

                        ,(self.email_txt.get(),self.password.get()))

            row=cur.fetchone()

            if row==None:

               messagebox.showerror('Error','Invalid Username And Password'

                                    ,parent=self.root)

               self.loginclear()

               self.email_txt.focus()

            else:

               self.appscreen()

               con.close()

         except Exception as es:

            messagebox.showerror('Error',f'Error Due to : {str(es)}'

                                 ,parent=self.root)

            

   def Register(self):



      Frame_login1=Frame(self.root,bg="white")

      Frame_login1.place(x=0,y=0,height=700,width=1366)

      

      self.img=ImageTk.PhotoImage(file="images/img2.JPG")

      img=Label(Frame_login1,image=self.img).place(x=0,y=0,width=1366,height=700)

      

      frame_input2=Frame(self.root,bg='white')

      frame_input2.place(x=320,y=130,height=450,width=630)



      label1=Label(frame_input2,text="Register User",font=('impact',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=45,y=20)



      label2=Label(frame_input2,text="Username",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label2.place(x=30,y=95)

      self.entry=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry.place(x=30,y=145,width=270,height=35)

      

      label3=Label(frame_input2,text="Password",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label3.place(x=30,y=195)

      self.entry2=Entry(frame_input2,font=("times new roman",15,"bold"),

                        bg='lightgray')

      self.entry2.place(x=30,y=245,width=270,height=35)



      label4=Label(frame_input2,text="Email-id",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label4.place(x=330,y=95)

      self.entry3=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry3.place(x=330,y=145,width=270,height=35)



      label5=Label(frame_input2,text="Confirm Password",

                   font=("Goudy old style",20,"bold"),fg='orangered',bg='white')

      label5.place(x=330,y=195)

      self.entry4=Entry(frame_input2,font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry4.place(x=330,y=245,width=270,height=35)



      btn2=Button(frame_input2,command=self.register,text="Register"

                  ,cursor="hand2",font=("times new roman",15),fg="white",

                  bg="orangered",bd=0,width=15,height=1)

      btn2.place(x=90,y=340)

        

      btn3=Button(frame_input2,command=self.loginform,

                  text="Already Registered?Login",

                  font=("calibri",10),bg='white',fg="black",bd=0)

      btn3.place(x=110,y=390)





   def register(self):

      if self.entry.get()==""or self.entry2.get()==""or self.entry3.get()==""or self.entry4.get()=="":

         messagebox.showerror("Error","All Fields Are Required",parent=self.root)

      elif self.entry2.get()!=self.entry4.get():

         messagebox.showerror("Error","Password and Confirm Password Should Be Same"

                              ,parent=self.root)

      else:

        

            con=pymysql.connect(host="localhost",user="root",password="214531",

                                database="tiffin")

            cur=con.cursor()

            cur.execute("select * from register where emailid=%s"

                        ,self.entry3.get())

            row=cur.fetchone()

            if row!=None:

               messagebox.showerror("Error"

               ,"User already Exist,Please try with another Email"

                                    ,parent=self.root)

               self.regclear()

               self.entry.focus()

            else:

               cur.execute("insert into register values(%s,%s,%s,%s)"

                           ,(self.entry.get(),self.entry3.get(),

                           self.entry2.get(),

                           self.entry4.get()))

               con.commit()

               con.close()

               messagebox.showinfo("Success","Register Succesfull"

                                   ,parent=self.root)

               self.regclear()

         



   def appscreen(self):



      Frame_login=Frame(self.root,bg="white")

      Frame_login.place(x=0,y=0,height=700,width=1366)
      self.img=ImageTk.PhotoImage(file="pics/mainpage2.jpg")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
      menubar = Menu(root)  
      file = Menu(menubar, tearoff=0)  
      file.add_command(label="Exit", command=root.quit)  
      e1=self.email_txt.get()
      menubar.add_cascade(label="Logout", menu=file)  
      definition = Menu(menubar, tearoff=0)  
      definition.add_command(label="view menu", command=self.user_definition) 
      #definition.add_separator()
          
                
      menubar.add_cascade(label="Order", menu=definition)  
        
      purchase = Menu(menubar, tearoff=0)  
      purchase.add_command(label="View Payment " ,command=self.pay1)  
      menubar.add_cascade(label="Payment", menu=purchase)  
        
      sales = Menu(menubar, tearoff=0)  
      sales.add_command(label="Feedback",command=self.feedbackk)  
      menubar.add_cascade(label="Feedback", menu=sales)  
      root.config(menu=menubar)
      l3=tk.Label(Frame_login,text=self.email_txt.get(),font=('impact',22),bg="white",fg="dark orange")
      l3.place(x=300,y=20)
      #grid(row=3,column=1)
      label2=Label(text="Welcome to ",font=('impact',22),bg="white",fg="dark orange")
      label2.place(x=300,y=80)
      label1=Label(text="FRAGRANCE TIFFIN SERVICE",font=('impact',22),bg="white",fg="dark orange")
      label1.place(x=300,y=160)
   def pay1(self):
          call(['python' , 'custreport.py'])
          
   def pay(self):
      import tkinter as ttk
      Frame_pay=Frame(self.root,bg="white")

      Frame_pay.place(x=0,y=0,height=700,width=1366)
      self.img=ImageTk.PhotoImage(file="pics/CaptureTiffin.png")
      img=Label(Frame_pay,image=self.img).place(x=0,y=0,width=1366,height=700)
      self.trv = ttk.Treeview(self,root)
      self.trv.place(relheight=1, relwidth=1)      
      treescrolly = tk.Scrollbar(Frame_pay, orient="vertical", command=self.trv.yview) # command means update the yaxis view of the widget
      treescrollx = tk.Scrollbar(Frame_pay, orient="horizontal", command=self.trv.xview) # command means update the xaxis view of the widget
      self.trv.configure(xscrollcommand=treescrollx.set, yscrollcommand=treescrolly.set) # assign the scrollbars to the Treeview Widge
      treescrollx.pack(side="bottom", fill="x") # make the scrollbar fill the x axis of the Treeview widget
      treescrolly.pack(side="right", fill="y") # make 
      self.trv["columns"] = ("1", "2", "3","4","5","6")
      self.trv['height']  =20
      # Defining heading
      self.trv['show'] = 'headings'
      
      # width of columns and alignment 
      self.trv.column("1", width = 30, anchor ='c')
      self.trv.column("2", width = 30, anchor ='c')
      self.trv.column("3", width = 30, anchor ='c')
      self.trv.column("4", width = 30, anchor ='c')
      self.trv.column("5", width = 30, anchor ='c')
      self.trv.column("6", width = 30, anchor ='c')


      
      # Headings  
      # respective columns
      self.trv.heading("1", text ="s_id")
      self.trv.heading("2", text ="cid")
      self.trv.heading("3", text ="cname")
      self.trv.heading("4", text ="number")  
      self.trv.heading("5", text ="address")
      self.trv.heading("6", text ="pin")
      ph1=tk.StringVar()
      label1=Label(root,text="blanc",font=('impact',32,'bold'),fg="black",bg='white')
      label1.place(x=50, y=70)
      label2=Label(root,text="select status",font=('impact',22,'bold'),fg="white",bg='black')
      label2.place(x=50, y=170)

      areaEntry = Entry(root, width=25, bd=5, font=('Arial', 15), textvariable = ph1)
      areaEntry.place(x=150, y=70)


      r1_v = tk.StringVar()
      r1 = tk.Radiobutton(root, text='paid', variable=r1_v, value="paid")
      r1.place(x=250, y=170) 
      r2 = tk.Radiobutton(root, text='unpaid', variable=r1_v, value="unpaid")
      r2.place(x=350, y=170)
      selectBtn = Button(root, text="Select", padx=35, pady=15, width=6,bd=1, font=('Arial', 15), bg="#EEEEEE", command=self.payment(r1_v,ph1))
      selectBtn.place(x=150, y=290)
   def payment(self,ph1,r1_v,trv):
         query="select * from plus2_bill WHERE cust_e='"+ph1.get()+"' and status='"+r1_v.get()+"'"
         r_set=my_conn.execute(query) # execute query with data
         for item in trv.get_children(): # delete all previous listings
            trv.delete(item)
         # to store total sale of the selected date
         for dt in r_set: 
            trv.insert("", 'end',iid=dt[0], text=dt[0],
            values =(dt[0],dt[1],dt[2],dt[3],dt[4],dt[5]))
            
      

   def feedbackk(self):
        self.feedback()

   def user_definition(self):
        import main_db
        
   def feedback(self):
        
      Frame_login=Frame(self.root,bg="white")

      Frame_login.place(x=0,y=0,height=700,width=1366)
      self.img=ImageTk.PhotoImage(file="pics/mainpage2.jpg")
      img=Label(Frame_login,image=self.img).place(x=0,y=0,width=1366,height=700)
      label1=Label(text=self.email_txt.get(),font=('impact',32,'bold'),

                   fg="black",bg='white')

      label1.place(x=45,y=20)



      label2=Label(text="comment bellow",font=("Goudy old style",20,"bold"),

                   fg='orangered',bg='white')

      label2.place(x=30,y=95)

      
      self.entry11=Entry(font=("times new roman",15,"bold"),

                       bg='lightgray')

      self.entry11.place(x=30,y=190,width=270,height=75)
      btn2=Button(command=self.feed,text="submit"

                  ,cursor="hand2",font=("times new roman",15),fg="white",

                  bg="orangered",bd=0,width=15,height=1)

      btn2.place(x=90,y=350)
   def feed(self):
        
    
      if self.entry11.get()=="":

         messagebox.showerror("Error","Please Fill The Comment",parent=self.root)
      else:
    
        
            con=pymysql.connect(host="localhost",user="root",password="214531",

                                database="tiffin")

            cur=con.cursor()

            

           

            cur.execute("insert into feedback values(%s,%s)"

                        ,(self.email_txt.get(),self.entry11.get()))

            con.commit()

            con.close()

            messagebox.showinfo("Success","comment Succesfull"

                                ,parent=self.root)

            self.regclear()

        
      
   def regclear(self):

      self.entry.delete(0,END)

      self.entry2.delete(0,END)

      self.entry3.delete(0,END)

      self.entry4.delete(0,END)

      self.entry11.delete(0,END)

   def loginclear(self):

      self.email_txt.delete(0,END)

      self.password.delete(0,END)

root=Tk() 
obj=Login(root)
root.mainloop()
