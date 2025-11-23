# Write a python program to check whether a year is a leap year or not

year = int(input("Enter Year : "))

if (year % 400 == 0) or (year % 100 != 0 and year % 4 == 0):
    print(year , "is Leap Year")
else:
    print(year , "is not Leap Year")