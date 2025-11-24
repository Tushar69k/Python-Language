'''
What are the various ways of passing arguments to a function? Write 
a function to display all prime numbers between a range which is
passed as arguments.
'''
def show_primes(start, end):
    print(f"Prime numbers between {start} and {end} are:")

    for num in range(start, end + 1):
        if num > 1:   # prime numbers are greater than 1
            for i in range(2, int(num ** 0.5) + 1):
                if num % i == 0:
                    break
            else:
                print(num, end=" ")

# ---- Driver Code ----
start = int(input("Enter start of range: "))
end = int(input("Enter end of range: "))

show_primes(start, end)
