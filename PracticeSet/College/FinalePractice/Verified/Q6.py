

def func2(ti) : 
    sums = sum(num for num in ti)
    print(f"sum is {sums}")
    avg = sums / len(ti)
    print(f"avg is {avg}")




ti = (2, 3, 4, 4 ,4,5 ,)
func2(ti)




nums = [1, 2, 3, 4]
square = []
for n in nums:
    square.append(n*n)
print(square)


square = [n*n for n in nums]