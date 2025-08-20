num = 5

for i in range(num):
    for j in range(num - 1 - i):
        print(" " , end=" ")

    for j in range(i+1):
        print("*" , end=" ")

    for j in range(i):
        print("*" , end=" ")
    print() 
                
 