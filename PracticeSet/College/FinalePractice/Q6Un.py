list = [1,[2,3,4],['a','b',[5,6]],7]
print(list)

list[1].append(9)
print(list)

list[2][2].remove(6)
print(list)

list[2].insert(2,'c')
print(list)

list[1].pop(1)
print(list)

del list[2][3][0]
print(list)

# Python function to return sum and average of numbers in a tuple

print("Python function to return sum and average of numbers in a tuple")

def sum_and_avg(t):
    total = 0
    for num in t:
        total += num   # manually adding each number
    avg = total / len(t)
    return total, avg

# Example
t = (10, 20, 30, 40, 69)
print(sum_and_avg(t))
