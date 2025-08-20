num = int(input("Enter the Number of stars row you have to Print : "))

print("\n\tPattern 1 \n")
for i in range(num):
    for j in range (i+1):
        print("*" , end=" ")
    print()
print()    



print("\n\tPattern 2 \n")
for i in range(num):

    for j in range (num-1-i):
        print(" " ,end=" ")

    for j in range(i+1):
        print("*" , end = " ")
    print()
print()

 

print("\n\tPattern 3 \n")
for i in range(num):
    for j in range (num-i):
        print("*" , end=" ")
    print()

    for j in range(i+1):
        print(" " , end = " ")
print()    



print("\n\tPattern 4 \n")
for i in range(num):
    for j in range (num - i):
        print("*" , end=" ")
    print()
print()  



print("\n\tPattern 5 \n")
for i in range(num):

    for j in range (num-1-i):
        print(" " ,end=" ")

    for j in range(i+1):
        print("*" , end = " ")
    
    for j in range(i+1-1):
        print("*" , end = " ")
    print()
print()



print("\n\tPattern 6 \n")
for i in range(num):
    for j in range(i):
        print(" " , end= " ")

    for j in range(num-i):
        print("*" , end= " ")

    for j in range(num - i -1):
        print("*" , end= " ")
    print()    
print()



print("\n\tPattern 7 \n")
for i in range(num-1):

    for j in range (num-1-i):
        print(" " ,end=" ")

    for j in range(i+1):
        print("*" , end = " ")
    
    for j in range(i+1-1):
        print("*" , end = " ")
    print()

for i in range(num):
    for j in range(i):
        print(" " , end= " ")

    for j in range(num-i):
        print("*" , end= " ")

    for j in range(num - i -1):
        print("*" , end= " ")
    print()    
print()



print("\n\tPattern 8 \n")
for i in range(num):
    for j in range(num):
        print("*" , end= " ")
    print()
print()        



print("\n\tPattern 9 \n")
for i in range(num-1):
    for j in range (i+1):
        print("*" , end=" ")
    print()
for i in range(num):
    for j in range (num - i):
        print("*" , end=" ")
    print()
print()  



print("\n\tPattern 10 \n")
for i in range(num-1):

    for j in range (num-1-i):
        print(" " ,end=" ")

    for j in range(i+1):
        print("*" , end = " ")
    print()

for i in range(num):
    for j in range (num-i):
        print("*" , end=" ")
    print()

    for j in range(i+1):
        print(" " , end = " ")
print()    



print("\n\tPattern 11 \n")
for i in range(1,num+1):
    for j in range(num):
        print(i , end= " ")
    print()
print()        



print("\n\tPattern 12 \n")
for i in range(num):
    for j in range(1 ,num+1):
        print(j , end= " ")
    print()
print()     



print("\n\tPattern 13 \n")
for i in range(1 ,num + 1):
    for j in range(i):
        print(i , end= " ")
    print()
print()       



print("\n\tPattern 14 \n")
for i in range(1 ,num + 1):
    for j in range( 1 ,i+1):
        print(j , end= " ")
    print()
print()   



print("\n\tPattern 15 \n")
for i in range(1 ,num + 1):
    for j in range(num-i):
        print(" " , end= " ")

    for j in range(1 ,i+1):   
        print(i , end=" ")
    print()
print()  



print("\n\tPattern 16 \n")
for i in range(1 ,num+1):
    for j in range(1 , i):
        print(" " , end= " ")

    for j in range(num-i+1):   
        print(i , end=" ")
    print()
print()  



print("\n\tPattern 17 \n")
for i in range(1 ,num+1):
    for j in range(num-i+1):
        print(i , end= " ")
    print()
print() 



print("\n\tPattern 18 \n")
for i in range(num , 0 , -1):
    for j in range(i):
        print(i , end= " ")
    print()
print()      



print("\n\tPattern 19 \n")
count = 1
for i in range(num):
    for j in range(i+1):
        print(count , end =" ")
        count+= 1
    print()
print()        



print("\n\tPattern 20 \n")   
for i in range(num):
    for j in range (num - i):
        if(i%2 == 0):
         print("0" , end=" ")
        else:
            print("1" ,end=" ")
    print()
print()  



print("\n\tPattern 21 \n")   
for i in range(num):
    for j in range (1 ,num - i +1):
          print(j , end=" ")
    print()
print()    



print("\n\tPattern 22 \n")  
for i in range(num , 0 , -1):
    for j in range(num, num - i, -1):  
        print(j , end=" ")
    print()
print()        



print("\n\tPattern 23 \n")  
c = 1
for i in range(num+1):
    for j in range(i):
        print(c ,end=" ")
        c += 2
    print()
print()    



print("\n\tPattern 24 \n")  
c2 = 2
for i in range(num+1):
    for j in range(i):
        print(c2 ,end=" ")
        c2 += 2
    print()
print()       



print("\n\tPattern 25 \n")  
for i in range(num):
    for j in range(num):
        print(chr(65+i) ,end=" ")
    print()
print()       



print("\n\tPattern 26 \n")  
for i in range(num):
    for j in range(num):
        print(chr(65+j) ,end=" ")
    print()
print()       



print("\n\tPattern 27 \n")  
for i in range(num):
    for j in range(i+1):
        print(chr(65+j) ,end=" ")
    print()
print()       



print("\n\tPattern 28 \n")  
for i in range(num):
    for j in range(i+1):
        print(chr(65+i) ,end=" ")
    print()
print()       



print("\n\tPattern 29 \n")  
for i in range(1 ,num+1):
    for j in range(i):
        print(i , end=" ")

    for j in range(num-i):
        print("*" ,end=" ")
    print()
print()     



print("\n\tPattern 30 \n")  
for i in range(1 ,num+1):
    for j in range(i):
        print(chr(64+i) , end=" ")

    for j in range(num-i):
        print("*" ,end=" ")
    print()
print()     



print("\n\tPattern 31 \n")  
for i in range(1 , num+1):
    for j in range(i):
        print(chr(64+i) , end=" ")

    for j in range(num-i+1):
        print(i ,end=" ")
    print()
print()     