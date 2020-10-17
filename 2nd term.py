#!/usr/bin/env python
# coding: utf-8

# ## Q33

# In[2]:


from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( ))
import pickle 


with open('emp1.dat', 'rb+') as fin:
    while True:
        try:
            record = pickle.load(fin)
            if record["EmpNO"] == 1251:
                record["Salary"] += 2000
                fin.seek(-1, 2)                    
                pickle.dump(record, fin)
                break
                
        except EOFError:
            break


# ## Q34

# In[5]:


from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( ))

import csv 
with open('Items.csv', 'w', newline='') as fout:
    csv_writer = csv.writer(fout)
    csv_writer.writerow(['ItemNo.', 'Name', 'Price', 'Category'])
    for i in range(5):
        print("Item number" + str(i+1))
        itemno = input('Enter Item No ')
        name = input('Name')
        price = int(input('Price'))
        category = input('Category')
        csv_writer.writerow([itemno,name, price, category])


# ## Q35 

# In[8]:


from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( )) 
import csv
with open('Items.csv', 'r') as fin:
    csv_reader = csv.reader(fin)

    itemno = input("Search for item no")
    for row in csv_reader:
        if row[0] == itemno:
            print(row)
            break


# ## Q36

# In[28]:


from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( )) 
import csv
with open('Items.csv', 'r') as fin:
    with open("highitems.csv", 'w') as fout:
        csv_reader = csv.reader(fin)
        csv_writer = csv.writer(fout)

        for i in csv_reader:
            try:
                if int(i[2]) > 250:
                    csv_writer.writerow(i)
            except:
                continue 


# ## Q37

# In[29]:


from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( ))

import csv 
with open('Items.csv', 'w', newline='') as fout:
    csv_writer = csv.writer(fout, delimiter='|')
    csv_writer.writerow(['ItemNo.', 'Name', 'Price', 'Category'])
    for i in range(5):
        print("Item number" + str(i+1))
        itemno = input('Enter Item No ')
        name = input('Name')
        price = int(input('Price'))
        category = input('Category')
        csv_writer.writerow([itemno,name, price, category])


# In[ ]:




