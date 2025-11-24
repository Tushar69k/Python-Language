   # Write a python program to check whether a g'ven number is prime or not.

print("Program to check whether a given number is empty or not")

flag = False

num = int(input("Enter a number : "))

for i in range( 2 , num - 1) :
    if num % i == 0 :
        flag = True 
        break


if flag : 
    print("Not Prime")
else : 
    print("Prime")    