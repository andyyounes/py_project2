import math
import random
x=int(input("Enter length of array: "))
s=[]
for i in range(x):
    s.append(random.randint(1,100))
print(s)
rev=0
for i in range(x):
    while(s[i]!=0):
        rem=s[i]%10
        rev=rev*10+rem
        s[i]=s[i]//10
    '''if n/10 python will print:1234/10=123,4
    if n//10 python will print the integer part only so 123'''
print("The inverse number is: ", rev)

