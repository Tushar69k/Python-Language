'''
What is exception handling in python? write a python program to
handle division by zero. value error and index error and display a
custom error message when an invalid input is provided which also
has finally block.
'''

def safe_division():
    try:
        # Taking input
        a = int(input("Enter the numerator: "))
        b = int(input("Enter the denominator: "))

        # Performing division
        result = a / b
        print("Result:", result)

        # List example for index error
        sample = [10, 20, 30]
        index = int(input("Enter index (0-2): "))
        print("Value at index:", sample[index])

    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

    except ValueError:
        print("Error: Invalid input! Only numbers are allowed.")

    except IndexError:
        print("Error: Index out of range! Choose 0, 1, or 2.")

    except Exception as e:
        print("Custom Error: Something went wrong!", e)

    finally:
        print("Program execution completed (finally block executed).")

# ---- Driver code ----
safe_division()
