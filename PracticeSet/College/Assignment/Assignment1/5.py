# Write a python program to check whether a year is a leap year or not

year = int(input("Enter Year : "))
num = year

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(num , "is Leap Year")
else:
    print(num , "is not Leap Year")