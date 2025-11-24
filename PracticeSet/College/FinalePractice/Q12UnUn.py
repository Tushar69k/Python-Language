'''
What are the various ways of passing arguments to a function? Write 
a function to display all prime numbers between a range which is
passed as arguments.
'''
def show_primes(start, end):
    print(f"Prime numbers between {start} and {end} are:")

    for num in range(start, end + 1):
        if num > 1:                           # primes start from 2
            for i in range(2, num):
                if num % i == 0:
                    break                     # not prime
            else:
                print(num, end=" ")

# Calling the function with positional arguments
show_primes(10, 50)
