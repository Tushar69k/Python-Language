print("\nSquare Pattern of Stars : \n")

n = 5
for i in range(n):
    for j in range(n):
        print("*", end=" ")
    print()
print()


print("Right-Angled Triangle : ")

n = 5 
for i in range (n + 1):
    for j in range (i):
        print("*" , end= " ")
    print()        
print()


print("Inverted Triangle : \n")

n = 5 
for i in range (n , 0 , -1):
    for j in range(i):
        print("*" , end= " ")
    print()   
print()


print("Number Triangle : \n")

n = 5 
for i in range(n+1):
    for j in  range(1 ,i+1):
        print(j , end= " ")
    print()    
print()



'Unknown Incompleted'

print("Pyramid Pattern : \n")

n = 5 
for i in range(n+1):
        print(" " * (n-i),end= "")
        print("* " * i)
print()



print("Pyramid Pattern : \n")

n = 5

# Upper part
for i in range(1, n+1):
    print(" " * (n - i) + "* " * i)

# Lower part
for i in range(n-1, 0, -1):
    print(" " * (n - i) + "* " * i)
