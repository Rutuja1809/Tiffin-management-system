import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import BOTH, END, LEFT
from my_connect import my_conn # database connection 
from my_invoice import my_invoice
from  datetime import date
sb=[]
font1=('Times',14,'normal')
font2=('Times',32,'bold')
my_w = tk.Tk()
my_w.geometry("1503x750+7+10") 

my_w.columnconfigure(0,weight=4)
my_w.columnconfigure(1,weight=2)
my_w.rowconfigure(0, weight=1) 
my_w.rowconfigure(1, weight=14) # change weight to 4
my_w.rowconfigure(2, weight=2)

frame_top=tk.Frame(my_w,bg='white')
frame_bottom=tk.Frame(my_w,bg='white')

frame_m_right=tk.Frame(my_w,bg='#f8fab4')
frame_m_left=tk.Frame(my_w,bg='#284474')

#placing in grid
frame_top.grid(row=0,column=0,sticky='WENS',columnspan=2)
frame_m_left.grid(row=1,column=0,sticky='WENS')
frame_m_right.grid(row=1,column=1,sticky='WENS')
frame_bottom.grid(row=2,column=0,sticky='WENS',columnspan=2)
trv = ttk.Treeview(frame_m_right, selectmode ='browse')
trv.grid(row=0,column=0,columnspan=2,padx=3,pady=2)
lr1=tk.Button(frame_m_right,text='Bill',font=font1,command=lambda:my_invoice)
lr1.grid(row=1,column=0,sticky='nw')        
# column identifiers 
trv["columns"] = ("1", "2","3")
trv.column("#0", width = 80, anchor ='w')
trv.column("1", width = 60, anchor ='w')
trv.column("2", width =50 , anchor ='c')
trv.column("3", width = 50, anchor ='c')
  
# Headings  
# respective columns
trv.heading("#0", text ="Item",anchor='w')
trv.heading("1", text ="Price",anchor='w')
trv.heading("2", text ="qty",anchor='c')
trv.heading("3", text ="Total",anchor='c')
def my_reset():
    for item in trv.get_children(): # loop all child items 
        trv.delete(item)        # delete them 
     # call the re-calculate and update the labels text
# Layout is over , sart placing buttons 
#path_image="G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\"
#img_top = tk.PhotoImage(file = path_image+"restaurant-3.png")
#bg=tk.PhotoImage(file=path_image+'bg2.png')

#img_l1 = tk.Label(frame_top,  image=img_top)
#img_l1.grid(row=0,column=0,sticky='nw',pady=1)

sel=tk.StringVar()
sel1=tk.StringVar()
sel2=tk.StringVar() # string variable for the Combobox
cb1=ttk.Combobox(frame_m_left,width=15,
    textvariable=sel,font=font2,)
cb1.grid(row=0,column=0,padx=10, pady=20) 

cb2=ttk.Combobox(frame_m_left,width=15,
    textvariable=sel1,font=font2)
cb2.grid(row=2,column=0,padx=10, pady=20) 

cb3=ttk.Combobox(frame_m_left,width=15,
    textvariable=sel2,font=font2)
cb3.grid(row=4,column=0,padx=10, pady=20) 

e1=tk.Entry(frame_m_left,width=4,font=font2)   
e1.grid(row=0,column=1)
def my_reset():
    global total, tax
    for item in trv.get_children():
        trv.delete(item)
    l1=[]
    for i in range(8):
        l1.append(tk.IntVar(value=0))
    for i in range(len(sb)):
        sb[i].config(textvariable=l1[i])

    for w in frame_m_right.grid_slaves(1):
        w.grid_remove()
    for w in frame_m_right.grid_slaves(2):
        w.grid_remove()    
    for w in frame_m_right.grid_slaves(3):
        w.grid_remove()
    dt=date.today().strftime('%Y-%m-%d') # todays date
    query="insert INTO  plus2_bill (Total,tax,`bill_date`) \
                  VALUES (%s,%s,%s)"
    data=[total,tax,dt]
    id=my_conn.execute(query,data)
    #print(total, tax)
    bill_no=id.lastrowid
    for i in dl:
        i.insert(3,bill_no)
        i.insert(4,dt)
    query="insert INTO plus2_sell(p_id,price,quantity,bill_no,bill_date)\
                  VALUES(%s,%s,%s,%s,%s)"
    id=my_conn.execute(query,dl)
    #print("Rows Added  = ",id.rowcount)  
    lr1=tk.Button(frame_m_right,text='Bill',font=font1,command=lambda:my_invoice(my_w,bill_no))
    lr1.grid(row=1,column=0,sticky='nw')                
dl=[]    
total,tax,final=0,0,0

lr1=tk.Label(frame_m_right,text='Total',font=font1)
lr1.grid(row=1,column=0,sticky='nw')
lr2=tk.Label(frame_m_right,text=str(total),font=font1)
lr2.grid(row=1,column=1,sticky='nw')
lr21=tk.Label(frame_m_right,text='Tax 10%',font=font1)
lr21.grid(row=2,column=0,sticky='nw')
tax=round(0.1*total,2)
lr22=tk.Label(frame_m_right,text=str(tax),font=font1)
lr22.grid(row=2,column=1,sticky='nw')
lr31=tk.Label(frame_m_right,text='Total',font=font2)
lr31.grid(row=3,column=0,sticky='nw')
final=round(total+tax,2)
lr32=tk.Label(frame_m_right,text=str(final),font=font2)
lr32.grid(row=3,column=1,sticky='nw')




def my_sum(): # Calculate total and tax part 
    total=0
    for line in trv.get_children(): # Loop through all items
        total=total+float(trv.item(line)['values'][2])
    tax=round(0.1*total,2)   # change the tax rate here 
    final=round(total+tax,2) # final price 
    lr2.config(text=str(total)) # show it at Label 
    lr22.config(text=str(tax))  # show it at Label
    lr32.config(text=str(final))# show it at Label 
def my_bill():
    global dl,total,tax,final 

    
    for i in range(len(sb)):
        if(int(sb[i].get())>0): 
            price=int(sb[i].get())*my_menu[i][2]
            total=round(total+price,2)
            my_str1=(str(my_menu[i][2]), str(sb[i].get()), str(price))
            trv.insert("",'end',iid=i,text=my_menu[i][1],values=my_str1)
            dl.append([my_menu[i][1],my_menu[i][3],int(sb[i].get())])
    
    
my_menu={} # Dictionary to store items with price
sb=[]
r,c,i=0,0,0
# show it at Label 
def my_add(): #adding item to bill 
    try:
        p_id=my_menu2[sel.get()][0]
        p_name=sel.get()
        price=e1.get()
        quantity=my_menu2[sel.get()][2]
    except:
        return None 
    if(int(quantity)>0 and len(p_name)>0 ):
        sub_total=round(float(price)*int(quantity),2)
        trv.insert("",'end',text=p_name,values=[price,quantity,sub_total])
        my_sum() 
        cb1.set('')
        e1.delete(0,END)
my_menu2={}
my_menu={}
def my_add1(): #adding item to bill 
    try:
        p_id=my_menu2[sel1.get()][0]
        p_name=sel1.get()
        price=e1.get()
        quantity=my_menu2[sel1.get()][2]
    except:
        return None 
    if(int(quantity)>0 and len(p_name)>0 ):
        sub_total=round(float(price)*int(quantity),2)
        trv.insert("",'end',text=p_name,values=[price,quantity,sub_total])
        my_sum()# 
        cb2.set('')
        e1.delete(0,END)
my_menu2={}
my_menu={}
def my_add2(): #adding item to bill 
    try:
        p_id=my_menu2[sel2.get()][0]
        p_name=sel2.get()
        price=e1.get()
        quantity=my_menu2[sel2.get()][2]
    except:
        return None 
    if(int(quantity)>0 and len(p_name)>0 ):
        sub_total=round(float(price)*int(quantity),2)
        trv.insert("",'end',text=p_name,values=[price,quantity,sub_total])
        my_sum() # 
        cb3.set('')
        e1.delete(0,END)
my_menu2={}
my_menu={} # Dictionary to store items with price
def show_items(cat): # Populating the Combobox 
    global my_menu,my_menu2
    my_menu.clear() # remove all items
    cb1.set('')
    e1.delete(0,END)
    r_set=my_conn.execute("select * FROM plus2_products WHERE \
       available=1 and  p_cat=1")
    
    for item in r_set:
        my_menu.update({item[0]:item[1]}) 
        my_menu2.update({item[1]:[item[0],item[1],item[3]]})
    options=list(my_menu.values())
    cb1.config(values=options)
    b1=tk.Button(frame_m_left,text='Add',font=font2,
     command=lambda:my_add())
    b1.grid(row=0,column=2,padx=10)
show_items(1)
r1_v = tk.IntVar(value=1) # We used integer variable here
def show_items(cat): # Populating the Combobox 
    global my_menu,my_menu2
    my_menu.clear() # remove all items
    cb2.set('')
    e1.delete(0,END)
    r_set=my_conn.execute("select * FROM plus2_products WHERE \
       available=1 and  p_cat=2")
    
    for item in r_set:
        my_menu.update({item[0]:item[1]}) 
        my_menu2.update({item[1]:[item[0],item[1],item[3]]})
    options=list(my_menu.values())
    cb2.config(values=options)
    b1=tk.Button(frame_m_left,text='Add',font=font2,
     command=lambda:my_add1())
    b1.grid(row=2,column=2,padx=10)
show_items(2)
def show_items(cat): # Populating the Combobox 
    global my_menu,my_menu2
    my_menu.clear() # remove all items
    cb3.set('')
    e1.delete(0,END)
    r_set=my_conn.execute("select * FROM plus2_products WHERE \
       available=1 and  p_cat=3")
    
    for item in r_set:
        my_menu.update({item[0]:item[1]}) 
        my_menu2.update({item[1]:[item[0],item[1],item[3]]})
    options=list(my_menu.values())
    cb3.config(values=options)
    b1=tk.Button(frame_m_left,text='Add',font=font2,
     command=lambda:my_add2())
    b1.grid(row=4,column=2,padx=10)
show_items(1)
r1_v = tk.IntVar(value=1) # We used integer variable here
r1_v = tk.IntVar(value=1) # We used integer variable here 

r1 = tk.Radiobutton(frame_bottom, text='Breakfast', variable=r1_v, value=1,command=lambda:show_items(1))
r1.grid(row=0,column=0) 

r2 = tk.Radiobutton(frame_bottom, text='Lunch', variable=r1_v, value=0,command=lambda:show_items(2))
r2.grid(row=0,column=1) 

r3 = tk.Radiobutton(frame_bottom, text='Dinner', variable=r1_v, value=5,command=lambda:show_items(3))
r3.grid(row=0,column=2)
b1=tk.Button(frame_bottom,text='Place Order',command=my_bill)
b1.grid(row=0,column=3,padx=10)
b2=tk.Button(frame_bottom,text='Confirm ( Reset)',command=my_reset)
b2.grid(row=0,column=4,padx=10)
my_w.mainloop()
