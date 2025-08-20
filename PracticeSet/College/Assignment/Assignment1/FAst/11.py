# Write a python program to demonstrate all operators –
# a) Arithmetic Operators
# b) Assignment Operators
# c) Comparison Operators
# d) Logical Operators
# e) Bitwise Operators
# f) Special Operators


# Python program to demonstrate all types of operators

print("\n--- a) Arithmetic Operators ---")
a = 10
b = 3
print("a + b =", a + b)   # Addition
print("a - b =", a - b)   # Subtraction
print("a * b =", a * b)   # Multiplication
print("a / b =", a / b)   # Division
print("a % b =", a % b)   # Modulus
print("a // b =", a // b) # Floor Division
print("a ** b =", a ** b) # Exponentiation

print("\n--- b) Assignment Operators ---")
x = 5
print("Initial x =", x)
x += 2
print("x += 2 ->", x)
x -= 1
print("x -= 1 ->", x)
x *= 3
print("x *= 3 ->", x)
x /= 2
print("x /= 2 ->", x)
x %= 4
print("x %= 4 ->", x)
x **= 2
print("x **= 2 ->", x)

print("\n--- c) Comparison Operators ---")
p = 7
q = 5
print("p == q ->", p == q)
print("p != q ->", p != q)
print("p > q  ->", p > q)
print("p < q  ->", p < q)
print("p >= q ->", p >= q)
print("p <= q ->", p <= q)

print("\n--- d) Logical Operators ---")
m = True
n = False
print("m and n ->", m and n)
print("m or n  ->", m or n)
print("not m   ->", not m)

print("\n--- e) Bitwise Operators ---")
x = 6   # 110 in binary
y = 3   # 011 in binary
print("x & y =", x & y)   # Bitwise AND
print("x | y =", x | y)   # Bitwise OR
print("x ^ y =", x ^ y)   # Bitwise XOR
print("~x =", ~x)         # Bitwise NOT
print("x << 1 =", x << 1) # Left Shift
print("x >> 1 =", x >> 1) # Right Shift

print("\n--- f) Special Operators ---")
list1 = [1, 2, 3]
list2 = [1, 2, 3]
list3 = list1
print("list1 is list3 ->", list1 is list3)     # Identity Operator
print("list1 is not list2 ->", list1 is not list2)
print("2 in list1 ->", 2 in list1)             # Membership Operator
print("5 not in list1 ->", 5 not in list1)
