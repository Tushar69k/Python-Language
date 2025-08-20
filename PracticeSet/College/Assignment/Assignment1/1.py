# Write a python program to find largest number among three and four numbers.

num1 = int(input("Enter 1 Number : "))
num2 = int(input("Enter 2 Number : "))
num3 = int(input("Enter 3 Number : "))

if(num1 > num2 and num1 > num3):
    print(num1 , "is greatest")
elif(num2 > num1 and num2 > num3):    
    print(num2 , "is greatest")
elif(num3 > num1 and num3 > num2):    
    print(num3 , "is greatest")