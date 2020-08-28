#1
from datetime import datetime 
import getpass 
print("Date: ",datetime.now( )) 
print("UserName: ",getpass.getuser( ))
#1 
def bubbleSort(arr): 
    n = len(arr) 
    for i in range(n):
        for j in range(0, n-i-1): 
            if arr[j] > arr[j+1] : 
            arr[j], arr[j+1] = arr[j+1], arr[j] 
d1 = {}
l1 =[]
for i in range(1,4):
    key = input("Enter NAME of student",i)
    l1.append(key)
    value = input("Enter MARKS of student",i)
    d1.[key]= value
bubblesort(l1)
for k in l1:
    print("Key",k)
    print('Value',d1[key])
#take input from user
d1 = {}
for i in range(5):
    k = input ('Key for the dictionary ')
    v = input ('Corresponding value for')
    d1[k] = v
print(d1)
#2
z=[]    
for row in range(7):    
    for column in range(7):     
        if (((row == 0 or row == 6) and column >= 0 and column <= 6) or row+column==6):  
               z.append('*')
        else:      
            z.append(" ")    
    for i range(7):
        z.append(" ")
print(z)


#3

l1 = []
for i in range(3):
    for j in range(4):
        for k in range(6):
            l1.append('*')    
print(l1)

#4
def volume(l = 1.0,b = 1.0,h =1.0):
    return(l*b*h)
l = float(input('Length of the Box'))
b = float(input('Width of the Box'))
h = float(input('Height of the Box'))
volume(l,b,h)
#5
def cube(a = ""):
    if a =="":
        return(2**3)
    else:
        return(a**3)

a = int(input('Please enter the first value'))
cube(a)

def equality(h,k):
    if h == k:
        return True
    else:
        return False
h = input('Please enter the first value')
k = input('Please enter the first value')
equality(h,k)

#6
def factors(x):
    l1 = []
    sm = 0
    for i in range(round(x/2)):
        if x%i == 0:
            l1.append(i)
    for i in l1:
        sm +=i
    if sm == x:
        print('Perfect Number')
    else :
        print('Not a Perfect Number')
x = int(input('Enter a number to check whether it is Perfect or not '))
factors(x)

#7
def execute(string):
    try:
        x = exec(string)
    execpt Exception as e:
        print("Error:", e)

string = str('Enter the code which you want to execute')
execute(string)

#8
def digit(n):
    try :
        count=0
        while(n>0):
            count=count+1
            n=n//10
        range_start = 10**(n-1)
        range_end = (10**n)-1
        return randint(range_start, range_end)
    except Exception as SyntaxError:
        print("Numbers can't start with 0 ")
        
print("The number of digits in the number are:",count)
n = int(input('Enter the number of digits '))
digit(n)

#9
def series(a,b):r
    diff = (a+b)/4
    return (a, a+diff, b-diff, b)

t = int(input('enter your first number of the series'))
k = int(input('enter your first number of the series'))
series(t,k)


#10
def prime(p):
    for i in range(2,round(p/2)):
        if p %i == 0:
            print("Not prime")
        else:
            print('Prime')

p = int(input("Enter the number to test primality"))
prime(p)


#11
def Isprime(N,a=2):
    if N == 1:
        print('Neither Prime nor composite')
    elif N == 2:
        return False
    elif N%2 == 0
        return False
    elif a>=N:
        return True
    
    else:
        return Isprime(N,a+1)    

N = int(input('Enter number to test primality'))

#12
def prdt(a,b):
    if b == 1:
        return a
    elif b ==0:
        return 0
    else:
        return prdt(a,b-1)
a = int(input('1st number'))
b = int(input('2nd number'))    

#13
l2 = []
def hailstone(n):
    if n == 1:
        l2.append(1)
        return l2
    elif n == 0:
        return 0
    elif n%2 == 0:
        n = (n/2)
        hailstone(n)
    elif n%2 != 0:
        n = 3*n +1
        hailstone(n)
        
n = int(input('Plase enter the number to start the sequence'))
hailstone(n)

#14
def remove_letter(s,l):
    k = s.replace(l, "")
    print(k)
    
string= str(input("Please enter your string  "))
letter =str(input("Please enter your letter  "))
remove_letter(string,letter)


#
    



from datetime import datetime
import getpass
print("Date: ",datetime.now( ))
print("UserName: ",getpass.getuser( ))

import massconversion
help(massconversion)
a = int(input("Please eneter value for convertion  "))
print('kgtotonne',end="  ")
massconversion.kgtotonne(a)
print('tonnetokg',end="  ")
massconversion.tonnetokg(a)
print('kgtopound',end="  ")
massconversion.kgtopound(a)
print('poundtokg',end="  ")
massconversion.poundtokg(a)






