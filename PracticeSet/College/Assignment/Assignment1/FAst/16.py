# Write a python program to print the Fibonacci sequence.
#  0,1,1,2,3,5,8,13,21,...

# Python program to print Fibonacci sequence

n = int(input("Enter number of terms: "))

# First two terms
a, b = 0, 1

print("Fibonacci sequence:")


for i in range(n):
    print(a, end=" ")
    a, b = b, a + b

# Self
# print(a , b , end=" ")
# for i in range(1 ,n):
#      c = a + b 
#      a = b 
#      b = c
#      print(c , end=" ")