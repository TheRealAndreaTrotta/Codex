people = [
    {"name": "harry", "house": "gryffindor"},
    {"name": "draco", "house": "slytherin"},
    {"name": "cedric", "house": "hufflepuff"},
]

'''
def f(person):
    return person["name"]

people.sort(key=f) 
'''

people.sort(key=lambda person: person["name"])

print(people)
# this wll raise an error because python doesn't know how to sort dictionaries by default
# that's why we provide a key function 