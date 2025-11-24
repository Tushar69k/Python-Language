
# a, b = 0 , 1 

# num = 10 

# for i in range(num) : 
#       print(a , end = " ")
#       a , b = b , a +b 
#     #   b = a + b 

def recur(num) : 
      if num <= 1 :
            return num 
      
      else : 
            return recur(num - 1) + recur(num - 2)
      
def show():
            
      numm = int(input("Enter Range : "))
      for i in range (numm) :
        print(recur(i) , end = " ")

  
show()