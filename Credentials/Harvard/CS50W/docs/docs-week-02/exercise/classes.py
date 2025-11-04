'''
class point():
    def __init__(self, x, y):
        self.x = x
        self.y = y

p = point(3, 4)
print(p.x)
print(p.y)
'''

class Flight():
    def __init__(self, capacity): #constructor method that initializes the object
        self.capacity = capacity  #we use self to refer to the object itself
        self.passegers = []

    def add_passenger(self, name): 
        if not self.available_seats(): #not is the equivalent of checking if it is 0
            return False
        self.passegers.append(name)
        return True

    def available_seats(self):
        return self.capacity - len(self.passegers)

flight = Flight(3)

people = ["Harry", "Ron", "Hermione", "Draco"]

for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")

#questo non è completo