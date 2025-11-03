import sys

try:
    x = int(input("x:"))
    y = int(input("y:"))
except ValueError:
    print("Error: Invalid input. Please enter numeric values.")
    sys.exit(1)

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")
    sys.exit(1)



print(f"{x} divided by {y} is {result}")