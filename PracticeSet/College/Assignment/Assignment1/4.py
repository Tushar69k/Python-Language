'''
Write a python program to check whether a number is even or odd using conditional
statement and using for and while loop
'''

num = int(input("Enter Number : "))

if(num % 2 == 0):
    print(num ,"is Even")
else : 
    print(num ,"is Odd")    


num1 = int(input("\n\tEnter number till you want to check number is even or odd : "))

for i in range(1 ,num1+1):
    if(i % 2 == 0):
     print(i ,"is Even")
    else : 
     print(i ,"is Odd")    
    

num2 = int(input("\n\tEnter number till you want to check number is even or odd : "))

count = 1
while count <= num2 :
    if(count % 2 == 0):
     print(count ,"is Even")
    else : 
     print(count ,"is Odd")    
    count += 1 