'''
write a python program where discount is calculated on the input amount. 
Rate program where discount is 5%  if the amount is less than 1000, and 10% if it is above 1000. 
'''

print("Program to Calculate Discount :: ")

amount = float(input("Enter Amount :  "))


if amount < 1000 :
    discount = 0.05 * amount 
elif amount > 1000 :   
    discount = 0.10 * amount    


finalamount = amount - discount    

print("Your discount for amount " , amount , "is " , discount , " and your final amount is " , finalamount)