'''
Chapter 4: Working with Lists

What its about:
    Looping with lists and working with them as a whole
    instead of each element like last chapter

'''

# Prompts and project notes

'''
# Section 1
# 4-1
pizza = ["chicken & Jalepenos",  "Supreme", "pepperoni", "Cheese", "Veggie", "Meat Lovers"]

for za in pizza:
    print(f"One choice of pizza is: {za}")

print("Pizza is pretty versitile.")

# 4-2
animals = ["Polar bear", "Brown bear", "Sun bear", "Moon bear", "Panda bear", "Koala bear"]
for bear in animals:
    print(f"Well Forrest, there are all types of bear like {bear}...")

print("all these animals are called bears")
'''

# Section 2
'''
# 4-3
for digit in range(20):
    print(digit + 1)

# 4-4
large = [digit for digit in range(1, 1000001)]
print(large)


# 4-5
large = [digit for digit in range(1, 1000001)]
print(sum(large))

# 4-6
odd = [oddity for oddity in range(1, 21, 2)]
print(odd)

# 4-7
triple = [trips for trips in range(3, 31, 3)]
print(triple)

# 4-8
cubes = [cube**3 for cube in range(1, 11)]
print(cubes)

# 4-9
# oops, I was doing this the whole time so will make this more complicated I guess
cubes_2 = []
for int in range(1, 11):
    cubes_2.append(int**3)

print(cubes_2)
'''

'''
# section 3
# 4-10
animals = ["Polar bear", "Brown bear", "Sun bear", "Moon bear", "Panda bear", "Koala bear"]
print(f"The first 3 elements of the list are: {animals[0:3]}")
print(f"The middle 3 elements of the list are: {animals[2:5]}")
print(f"The last 3 elements of the list are: {animals[3:]}")

# 4-11
pizza = ["chicken & Jalepenos",  "Supreme", "pepperoni", "Cheese", "Veggie", "Meat Lovers"]
friends_pizza = ["chicken & Jalepenos",  "Supreme", "pepperoni", "Cheese", "Veggie", "Meat Lovers"]

pizza.append("Margarita")
friends_pizza.append("Chicago")
print(pizza)
print(friends_pizza)

# 4-12
    # this is to print them out different so no
'''

# Section 4
# 4-13
    # same thing as 4-12 but slightly different, still no

# 4-14
    # this says go read pep 0008 for style guidlines

# 4-15
    # my editor is already set up, but it recommends making changes in the case it isnt.


# Errors and fixes

# 4-3
    # not really an error but  to print numbers with range
    # it starts at 0 and ends 1 digit before your asked one
    # so to print, I added 1 in the print box

# 4-4
    # to add the list of all the numbers you need to do the
    # little for loop inside, cant just say [range()]

# 4-10
    # not an error but Note: list slicing is inclusive in the front
    # and exclusive to the rear number

# 4-11
    # I know what happened!!!! Excited for that reason.
    # I added pizzas to the 2 different list but they were
    # added to both
    # lists are pointers so when I assigned the new pizzas
    # to the old, they were pointing at the same place.
    # I need to copy paste the actual list to see a difference.


