#!/usr/bin/env python
# coding: utf-8

# ## Q38

# In[10]:


from datetime import datetime 
import getpass 
print("Date: ",datetime.now( )) 
print("UserName: ",getpass.getuser( ))
print() 
def q38():
    Runs = [[0, 6, 4, 1, 0, 0], [3, 0, 2, 0, 0, 0], [0, 0, 4, 4, 0, 1], [0, 0, 0, 1, 0, 0], [0, 0, 0, 0, 0, 0]]
    count = over = total= 0
    l = []
    for i in Runs:
        temp = 0
        for j in i:
            temp +=j
            total +=j
        l.append(temp)
        if temp > count:
            count,over = temp, Runs.index(i)+1
    l.sort()
    print("Highest score was",count,'in the over ',over)
    print("Minimun runs",l[0])
    print("TOTAL score was ", total )
q38()


# ## Q39

# In[4]:


from datetime import datetime 
import getpass 
print("Date: ",datetime.now( )) 
print("UserName: ",getpass.getuser( ))
print()
def q39():
    def afind(arr):
        for i in arr:
            if i[0] == 'A':
                print(i)
    afind(['Ahemdabad','Agra','Alipura','Dhaka','Delhi','Zila'])
    
q39()


# ## Q44

# In[6]:


from datetime import datetime 
import getpass 
print("Date: ",datetime.now( )) 
print("UserName: ",getpass.getuser( ))
print() 
def q44():
    import random
    print("Yummy programme")
    print("1.Order a meal \n 2.Waiting Queue \n 3.Order is Ready \n Exit")
    q  = []
    while True:
        x = int(input("Enter any one of the above options "))
        if x == 1:
            a = random.randint(100,999)
            print("Your order number is", a)
            q.append(a)
        elif x ==2:
            print("The order list", q)
        elif x == 3:
            if q==[]:
                print("No orders in queue")
                continue 
            else:
                a = q.pop(0)
                print("Order is ready ", a )
        elif x ==4:
            break 
        else:
            print("Please give a valid input")
            continue
q44()
print("EOF")


# ## q43

# In[8]:


from datetime import datetime 
import getpass 
print("Date: ",datetime.now( )) 
print("UserName: ",getpass.getuser( ))
print() 
def q43():
    string  = str(input("Enter your string "))
    stack  = []
    for i in string:
        stack.append(i)
    print("Your orginal string", string)
    for i in range(len(string)):
        print(stack.pop(-1),end='')
q43()


# ## Q45

# In[9]:


from datetime import datetime 
import getpass 
print("Date: ",datetime.now( )) 
print("UserName: ",getpass.getuser( ))
print() 
def q45():
    print("URL HISTORY")
    print(" 1.Go to new URL \n 2.History \n 3.Go Back \n 4.Exit")
    stack  = []
    while True:
        x = int(input("Enter any one of the above options "))
        if x == 1:
            print("New URL")
            a = input("Enter your URL")
            stack.append(a)
        elif x ==2:
            print("HISTORY", stack)
        elif x == 3:
            if stack == []:
                print("No URLs Visited till now")
            else:
                a = stack.pop(-1)
                print("Last visited ", a )
        elif x ==4:
            break 
        else:
            print("Please give a valid input")
            continue
q45()
print("EOF")


# ## Q40

# In[13]:


from datetime import datetime 
import getpass 
print("Date: ",datetime.now( )) 
print("UserName: ",getpass.getuser( ))
print() 
def q40():
    maxlen = 5
    stack= []
    print("Menu")
    print(" 1.Insert Element \n 2.Delete Element \n 3.Display Stack \n 4.Exit")

    while True:
        option = int(input("Enter one of the options  "))
        if option == 1:
            if len(stack)== maxlen:
                print("Overflow")
            else:
                num = int(input("Enter admission number  "))
                name  = input("Enter name of the student ")
                stack.append((num,name))
        elif option ==2:
            if stack == []:
                print("Underflow")
            else:
                print("Deleted the element  ", stack.pop())
        elif option ==3 :
            print(stack)
        elif option == 4:
            break
        else:
            print("Please enter a valid input ")
            continue
q40()


# ## Q41

# In[16]:


from datetime import datetime 
import getpass 
print("Date: ",datetime.now( )) 
print("UserName: ",getpass.getuser( ))
print()
def q41():
    l = input("Enter your list separated by commas").split()
    print('Your list',l)
    def insertq(arr,data):
        arr.append(data)
    def deleteq(arr):
        if arr == []:
            print("Empty list")
        else:
            return arr.pop()
    data = input("Enter data that needs to be added ")
    insertq(l,data)
    print('Updated list',l)
    print('Deleting data')
    print(deleteq(l))
q41()


# ## Q42

# In[ ]:


def q42():
    stack = []
    def Make_Package(pack):
        stack.append(pack)

    def Make_Pop():
        if stack == []:
            return ("No elements in the stack ")
        else:
            return stack.pop()
    def Display():
        return stack 
    #Deleting to test underflow
    print(Make_Pop())
    #Adding three packs
    Make_Package("Bro")
    Make_Package("Code")
    Make_Package("Jones")
    #Displaying the stack 
    print(Display())
    #Deleting pack
    print(Make_Pop())
    #Displaying the stack 
    print(Display())
q42()

