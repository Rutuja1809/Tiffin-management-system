
# coding: utf-8

# In[1]:

import pandas as pd
import numpy as np
from MDBS import *
from time import ctime
initialization()
initial_db()
initialize_order_db()
add_order(0,0,0,0,0);


# In[2]:

print("Welcome")
reg_no = input('Enter your Registration Number: ')

try:
    student_info = student_detail(reg_no)
except:
    print('Access Denied')
else:
    print('Hello '+student_info['Name'])
    print('Enter your choice as mentioned below')
    print('1. Order\n2. Account Details')
    choice = input()

    if(choice == '1'):
        total_amount = 0.00
        ord_detail = view_order_db()
        prev_token = ord_detail.index.values.tolist()
        prev_token = prev_token[-1]
        items = []
        while(1):
            df = view_menu_db()
            print(df)
            item_id = input('Enter the IDs of the item you want to order (seperate IDs using (,)): ')
            item_id_l = item_id.split(',')
            for o in item_id_l:
                items.append(df.loc[o]['Item'])
                total_amount = total_amount + order_amt(o)  
            more = input('If you want to order more enter 0 else to confirm order enter 1: ')
            if(more == '0'):
                continue
            else:
                debit(reg_no,total_amount)
                add_order((prev_token+1),ctime(),reg_no,items,total_amount)
                print('You ordered: ')
                for i in items:
                    print(i)
                print('Your total amount is: '),(total_amount)
                print('Your token number: '),(prev_token+1)
                break
    elif(choice == '2'):
        print(student_detail(reg_no))
    else:
        print('Invalid Input')


# In[ ]:



