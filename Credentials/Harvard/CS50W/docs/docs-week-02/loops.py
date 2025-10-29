'''
for i in [0, 1, 2, 3, 4, 5]:
    print(i) 

# The code above uses a for loop to iterate over a list of numbers from 0 to 5
# and prints each number on a new line.
# but this is better written with range()

for i in range(6):
    print(i)
    
# The code above uses a for loop with range() to iterate over numbers from 0 to 5

'''
'''
names = ["Alice", "Bob", "Charlie", "Diana"]

for name in names:
    print(name)
# The code above uses a for loop to iterate over a list of names
# and prints each name on a new line.
'''

name = "harry"

for character in name:
    print(character)
# The code above uses a for loop to iterate over each character in the string "harry"
# and prints each character on a new line.
# if i dont't want to print a new line for each character, i can use end=""

for character in name:
    print(character, end="")
# The code above uses a for loop to iterate over each character in the string "harry
# and if i don't want to see "%n" after each character, i use end="" to print all characters on the same line without spaces.

print()  # just to add a new line after the previous output
# The code above prints a new line to separate the previous output from any subsequent output.