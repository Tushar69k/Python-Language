num = 5

print("\t\nPattern 1\t")
for i in range (num):
    for j in range(i+1):
        print("*" , end=" ")
    print()
print()


print("\t\nPattern 2\t")
for i in range(num):
    for j in range(num-1-i):
        print(" " , end=" ")

    for j in range(i+1):
        print("*" , end=" ")
    print()
print()


print("\t\nPattern 3\t")
for i in range(num):
    for j in range(i):
        print(" " , end=" ")

    for j in range(num-i):
        print("*" , end=" ")
    print()
print()


print("\t\nPattern 4\t")
for i in range(num):
    for j in range(num-i):
        print("*" , end=" ")
    print()    
print()


print("\t\nPattern 8\t")
for i in range(num):
    for j in range(num):
        print("*" , end=" ")
    print()    
print()

