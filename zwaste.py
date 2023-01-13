
# coding: utf-8

# In[1]:

import pandas as pd
from MDBS import *


# In[2]:

print('Welcome')
print('1. New Registration\n2. Remove a Registration\n3. Update Credits\n4. History\n5. Access Students Database')
choice = input('Enter a choice from above: ')
if(choice == '1'):
    reg_no = input('Enter the registration number: ')
    name = input('Enter the name: ')
    fee = int(input('Enter the amount paid: '))
    add_student(reg_no,name,fee)
elif(choice == '2'):
    reg_no = input('Enter the registration number: ')
    remove_student(reg_no)
elif(choice == '3'):
    reg_no = input('Enter the registration number: ')
    fee = int(input('Enter the amount paid: '))
    credit(reg_no,fee)
elif(choice == '4'):
    print('1. Student Order History\n2. Orders Placed History')
    his_choice = input('Enter your choice: ')
    if(his_choice == '1'):
        reg_no = input('Enter the registration number: ')
        try:
            print(student_order_history(reg_no))
        except:
            print('No orders placed yet')
            #print(student_order_history(reg_no))
    elif(his_choice == '2'):
        print(view_order_db())
    else:
        print('Invalid Input')
elif(choice == '5'):
    print(view_db())
else:
    print('Invalid Input')


# # 
