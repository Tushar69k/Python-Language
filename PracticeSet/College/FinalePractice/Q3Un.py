# TUSHAR

num = 5

for i in range(num) : 

   for j in range(num - 1 - i):
        print(" " , end=" ")

   for j in range(i+1):
        print("*" , end=" ")

   for j in range(i):
        print("*" , end=" ")
   print()    



print("\n Another Way :: \n")

for i in range ( 1 , num+1) : 
     print("  " * (num - i) , end= " ")
     print(" *" * ((i*2)-1) , end = " ") 
     print()