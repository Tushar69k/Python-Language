print("Fibonacchi Series Recursive Function")



def Recursivefun(num) : 
    if num <= 1 : 
        return num 
    else : 
        return Recursivefun(num - 1) + Recursivefun(num - 2)
    

def PrintRecursive() :
  term = int(input(" Till how many terms you need recursive Function : "))
  for i in range(term) :
    print(Recursivefun(i) ,end= " ")


PrintRecursive()