# Write a python program to check whether a number is prime or not

# Simple Python program to check prime number

num = int(input("Enter a number: "))

if num <= 1:
    print(num, "is not a prime number")
else:
    count = 0
    for i in range(2, num):
        if num % i == 0:
            count = 1
            break

    if count == 0:
        print(num, "is a prime number")
    else:
        print(num, "is not a prime number")
