# Write a python program to calculate profit or loss.

cp = int(input("Enter the Cost Price : "))
sp = int(input("Enter the Selling Price : "))

profit = sp - cp  
loss = cp - sp 


if( sp > cp):
    print("you are in profit")
    print("Your Profit is : " , profit , " rs")
    print("Your Profit is " , ((profit/cp) * 100) , "%")
else : 
    print("you are in loss")
    print("Your loss is : " , loss , " rs")
    print("Your loss is " , ((loss/cp) * 100) , "%")


