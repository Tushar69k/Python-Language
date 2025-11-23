# Write a python program to calculate the sum of first 50 odd and even numbers.

# Python program to calculate sum of first 50 odd and even numbers

# Sum of first 50 odd numbers
sum_odd = 0
for i in range(1, 51):   # 1 to 50
    sum_odd += 2*i - 1   # formula for ith odd number

# Sum of first 50 even numbers
sum_even = 0
for i in range(1, 51):   # 1 to 50
    sum_even += 2*i      # formula for ith even number

print("Sum of first 50 odd numbers =", sum_odd)
print("Sum of first 50 even numbers =", sum_even)


se = 0
so = 0
for i in range(1,51):
    if(i % 2 == 0):
        se += i
    else : 
        so += i    
print("Sum of first 50 odd numbers =", so)
print("Sum of first 50 even numbers =", se)