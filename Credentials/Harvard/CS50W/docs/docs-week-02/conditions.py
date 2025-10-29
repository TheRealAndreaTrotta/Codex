number = input("Enter a number: ")
try:                                                # Attempt to convert input to a float
    number = float(number)                          # Convert input to float
    if number > 0:                                  # Check if the number is positive
        print("The number is positive.")
    elif number < 0:                                # Check if the number is negative 
        print("The number is negative.")
    else:
        print("The number is zero.")
except ValueError:                                  # Handle the case where conversion to float fails
    print("That's not a valid number.")