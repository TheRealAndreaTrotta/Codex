while True:
    string = input("Enter a number (q to quit): ")

    if string.lower() == "q":
        break

    try:
        # i must use parse with replace to handle both comma and dot as decimal separators 
        # e.g., "3.14" and "3,14"
        # thanks to this, both formats will be correctly interpreted as floats
        # indeed, this approach ensures that users from different locales can input numbers in their familiar format
        # the "," is recognized as a string character, so we replace it with "." before conversion
        x = float(string.replace(",", "."))  # <-- PARSE WITH REPLACE
    except ValueError:
        print("That's not a valid number.")
        continue

    if x > 0:
        print("The number is positive.")
    elif x < 0:
        print("The number is negative.")
    else:
        print("The number is zero.")

# The code above repeatedly prompts the user to enter a number until they choose to quit by entering 'q'.
# It attempts to convert the input to a float, handling both '.' and ',' as decimal separators.
# If the conversion fails, it informs the user that the input is not a valid number.
# If the conversion is successful, it checks whether the number is positive, negative, or zero and prints the appropriate message.
# i use parse with replace to handle both comma and dot as decimal separators.
