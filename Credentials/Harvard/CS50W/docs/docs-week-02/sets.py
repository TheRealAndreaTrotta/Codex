# create an empty set
s = set()

#add elements to the set
s.add(1)
s.add(2)
s.add(3)
s.add(4)

s.add(2)  
# adding a duplicate element, will have no effect follow the mathematical definition 
# of a set that contains only unique elements

print(s)

s.remove(3)  # remove element 3 from the set

print(s)

print(f"The set has {len(s)} elements.")  # print the number of elements in the set