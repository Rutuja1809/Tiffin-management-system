
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np


# In[2]:

def initialization():
    st_db = pd.DataFrame(columns=['Reg No.','Name','Credits'])
    st_db.to_csv('st_db.csv')

# In[3]:

def add_student(reg_no,name,credits):
    st_db = view_db()
    st_db = st_db.reset_index()
    st_db = st_db.append(pd.DataFrame([[reg_no,name,credits]],columns=st_db.columns))
    st_db.to_csv('st_db.csv')
    st_db = st_db.set_index('Reg No.')
    return st_db


# In[4]:

def initial_db():
    add_student('15BEC0260','Abhinav Kumar',3500)
    add_student('15BEC0124','Aditi Bhardwaj',3500)
    add_student('15BEC0242','Animesh Kumar',3500)
    add_student('15BEC0057','Vaishali Shukla',3500)
    #df = pd.read_csv('st_db.csv',index_col=['Reg No.']) 
    #df = df.drop('Unnamed: 0',axis=1)
    #df.to_csv('st_db.csv')
    #return df


# In[5]:

def remove_student(reg_no):
    st_db = view_db()
    st_db = st_db.drop(reg_no)
    st_db.to_csv('st_db.csv')
    return st_db


# In[6]:

def view_db():
    df = pd.read_csv('st_db.csv',index_col=['Reg No.']) 
    try:
        df = df.drop('Unnamed: 0',axis=1)
    except:
        return df
    else:
        return df


# In[7]:

def student_detail(reg_no):
    df = view_db()
    return df.loc[reg_no]


# In[8]:

def debit(reg_no,amt):
    df = view_db()
    curr_val = int(df.loc[reg_no]['Credits'])
    if(curr_val>100):
        df.set_value(reg_no,'Credits',curr_val-amt)
    else:
        print("Sorry, Insufficient Credit Balance")
    df.to_csv('st_db.csv')
    return df    


# In[9]:

def credit(reg_no,amt):
    df = view_db()
    curr_val = int(df.loc[reg_no]['Credits'])
    df.set_value(reg_no,'Credits',curr_val+amt)
    df.to_csv('st_db.csv')
    return df   


# In[10]:

def view_menu_db():
    menu_db = pd.read_csv('menu_db.csv',index_col=['Id'])
    return menu_db


# In[11]:

def order_amt(order_id):
    menu_db = view_menu_db()
    return float(menu_db.loc[order_id]['Price'])


# In[12]:

def generate_token(curr_token):
    curr_token = curr_token+1
    return curr_token


# In[13]:

def initialize_order_db():
    order_db = pd.DataFrame(columns=['Order No.','Time','Reg. No.','Order','Amount'])
    #order_db.set_index('Order No.')
    order_db.to_csv('orderdb.csv')


# In[14]:

def view_order_db():
    df = pd.read_csv('orderdb.csv',index_col=['Order No.']) 
    try:
        df = df.drop('Unnamed: 0',axis=1)
    except:
        return df
    else:
        return df


# In[16]:

def add_order(order_no,time,reg_no,order,amt):
    df = view_order_db()
    df = df.reset_index()
    df = df.append(pd.DataFrame([[order_no,time,reg_no,order,amt]],columns=df.columns))   
    df.to_csv('orderdb.csv')
    df = df.set_index('Order No.')
    return df


# In[30]:

def student_order_history(reg_no):
    df = view_order_db()
    df.reset_index()
    df = df.set_index('Reg. No.')
    return df.loc[reg_no]

