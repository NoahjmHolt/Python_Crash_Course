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
# 4-3
for digit in range(20):
    print(digit + 1)

# 4-4
large = [digit for digit in range(1, 1000001)]
print(large)

# Errors and fixes

# 4-3
    # not really an error but  to print numbers with range
    # it starts at 0 and ends 1 digit before your asked one
    # so to print, I added 1 in the print box

# 4-4
    # to add the list of all the numbers you need to do the
    # little for loop inside, cant just say [range()]



