import hogwarts

for student in hogwarts.houses:
    print(f"{student} is in {hogwarts.houses[student]}")
print()
#here i count the keys and the values in the dictionary
#so basically i am counting how many students are there in the dictionary


for student in hogwarts.houses:
    print(f"{student}")
print()
#here i count the keys in the dictionary

hogwarts.houses["Hermione"] = "Gryffindor"

print(f"Number of students: {len(hogwarts.houses)}")