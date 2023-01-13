import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import BOTH, END, LEFT

menu={0:['item One',20],1:['Item Two',40],2:['Item Three',30],
3:['Item Four',20],4:['Item five',30],5:['Item Six',20],
6:['Item Seven',40],7:['Item eight',30]}
sb=[]

my_w = tk.Tk()
my_w.geometry("1000x800") 

my_w.columnconfigure(0,weight=8)
my_w.columnconfigure(1,weight=2)
my_w.rowconfigure(0, weight=1) 
my_w.rowconfigure(1, weight=12) # change weight to 4
my_w.rowconfigure(2, weight=1)

frame_top=tk.Frame(my_w,bg='white')
frame_bottom=tk.Frame(my_w,bg='white')

frame_m_right=tk.Frame(my_w,bg='#f8fab4')
frame_m_left=tk.Frame(my_w,bg='#bfedf2')

#placing in grid
frame_top.grid(row=0,column=0,sticky='WENS',columnspan=2)
frame_m_left.grid(row=1,column=0,sticky='WENS')
frame_m_right.grid(row=1,column=1,sticky='WENS')
frame_bottom.grid(row=2,column=0,sticky='WENS',columnspan=2)
trv = ttk.Treeview(frame_m_right, selectmode ='browse')
trv.grid(row=0,column=0,columnspan=2,padx=3,pady=2)

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
    for item in trv.get_children():
        trv.delete(item)
    #for i in range(len(sb)):
    #    sb[i].config(textvariable=0)    # reset spinbox 
    l1=[]
    for i in range(8):
        l1.append(tk.IntVar(value=0))
    for i in range(len(sb)):
        print(sb[i].config(textvariable=l1[i]))

    for w in frame_m_right.grid_slaves(1):
        w.grid_remove()
    for w in frame_m_right.grid_slaves(2):
        w.grid_remove()    
    for w in frame_m_right.grid_slaves(3):
        w.grid_remove()
    
def my_bill():
    total=0
    for item in trv.get_children():
        trv.delete(item)
    for i in range(len(sb)):
        if(int(sb[i].get())>0):
            price=int(sb[i].get())*menu[i][1]
            total=total+price
            my_str1=(str(menu[i][1]), str(sb[i].get()), str(price))
            trv.insert("",'end',iid=i,text=menu[i][0],values=my_str1)
    lr1=tk.Label(frame_m_right,text='Total',font=font1)
    lr1.grid(row=1,column=0,sticky='nw')
    lr2=tk.Label(frame_m_right,text=str(total),font=font1)
    lr2.grid(row=1,column=1,sticky='nw')
    lr21=tk.Label(frame_m_right,text='Tax 10%',font=font1)
    lr21.grid(row=2,column=0,sticky='nw')
    tax=0.1*total
    lr22=tk.Label(frame_m_right,text=str(tax),font=font1)
    lr22.grid(row=2,column=1,sticky='nw')
    lr31=tk.Label(frame_m_right,text='Total',font=font2)
    lr31.grid(row=3,column=0,sticky='nw')
    final=total+tax
    lr32=tk.Label(frame_m_right,text=str(final),font=font2)
    lr32.grid(row=3,column=1,sticky='nw')
    
        
# Layout is over , sart placing buttons 
#path_image="G:\\My Drive\\testing\\plus2_restaurant_v1\\images\\"
font1=('Times',20,'normal')
font2=('Times',32,'bold')
pdx,pdy=40,5
#img_top = tk.PhotoImage(file = path_image+"restaurant-3.png")
#bg=tk.PhotoImage(file=path_image+'bg.png')

#c1 = tk.Canvas(frame_m_left,width=1000,height=500)
#c1.grid(row=0,column=0,columnspan=4,rowspan=4,sticky='nw',padx=0)
#c1.create_image(0,0,image=bg,anchor='nw')

#img_l1 = tk.Label(frame_top,  image=img_top)
#img_l1.grid(row=0,column=0,sticky='nw',pady=1)

#img_menu1=tk.PhotoImage(file=path_image+"food-item-1.png")
#img_menu2=tk.PhotoImage(file=path_image+"food-item-2.png")
#img_menu3=tk.PhotoImage(file=path_image+"food-item-3.png")
#img_menu4=tk.PhotoImage(file=path_image+"food-item-4.png")
#img_menu5=tk.PhotoImage(file=path_image+"food-item-5.png")
#img_menu6=tk.PhotoImage(file=path_image+"food-item-6.png")
#img_menu7=tk.PhotoImage(file=path_image+"food-item-7.png")
#img_menu8=tk.PhotoImage(file=path_image+"food-item-8.png")

menu1=tk.Button(frame_m_left,text='Item 1')
menu1.grid(row=0,column=0,sticky='nw',padx=pdx,pady=pdy)    
menu2=tk.Button(frame_m_left,text='Item 2')
menu2.grid(row=0,column=1,sticky='nw',padx=pdx,pady=pdy)
menu3=tk.Button(frame_m_left,text='Item 3')
menu3.grid(row=0,column=2,sticky='nw',padx=pdx,pady=pdy)
menu4=tk.Button(frame_m_left,text='Item 4')
menu4.grid(row=0,column=3,sticky='nw',padx=pdx,pady=0)
sv1=tk.IntVar()
sb1 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv1)
sb1.grid(row=1,column=0,sticky='nw',padx=pdx,pady=0)
sb.append(sb1)    
sv2=tk.IntVar()
sb2 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv2)
sb2.grid(row=1,column=1,sticky='nw',padx=pdx,pady=0)
sb.append(sb2)    
sv3=tk.IntVar()
sb3 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv3)
sb3.grid(row=1,column=2,sticky='nw',padx=pdx,pady=0)
sb.append(sb3)    
sv4=tk.IntVar()
sb4 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv4)
sb4.grid(row=1,column=3,sticky='nw',padx=pdx,pady=0)
sb.append(sb4)    
menu5=tk.Button(frame_m_left,text='item 5')
menu5.grid(row=2,column=0,sticky='nw',padx=pdx,pady=pdy)
menu6=tk.Button(frame_m_left,text='item 6')
menu6.grid(row=2,column=1,sticky='nw',padx=pdx,pady=pdy)
menu7=tk.Button(frame_m_left,text='item 7')
menu7.grid(row=2,column=2,sticky='nw',padx=pdx,pady=pdy)
menu8=tk.Button(frame_m_left,text='item 8')
menu8.grid(row=2,column=3,sticky='nw',padx=pdx,pady=pdy)
sv5=tk.IntVar()
sb5 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv5)
sb5.grid(row=3,column=0,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb5)
sv6=tk.IntVar()
sb6 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv6)
sb6.grid(row=3,column=1,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb6)
sv7=tk.IntVar()
sb7 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv7)
sb7.grid(row=3,column=2,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb7)
sv8=tk.IntVar()
sb8 = tk.Spinbox(frame_m_left,from_=0,to_=5,font=font1,width=1,textvariable=sv8)
sb8.grid(row=3,column=3,sticky='nw',padx=pdx,pady=pdy)
sb.append(sb8)
b1=tk.Button(frame_m_left,text='Get Bill',command=my_bill)
b1.grid(row=4,column=1)
b2=tk.Button(frame_m_left,text='Confirm ( Reset)',command=my_reset)
b2.grid(row=4,column=2)
my_w.mainloop()
