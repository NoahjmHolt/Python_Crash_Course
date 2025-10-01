
'''
Chapter 6: Dictionaries

What its about:
    how dictionaries work, connecting info modification and the like

Never experimented with dictionaries much in school so I am excited to give it a try
and learn more about them

'''

# 6-1

Jerry = {
    "first_name": "Jerry",
    "last_name": "Jones",
    "city": "Jerryville"
}

# 6-2
# this is just to create another dict and not use it like 6-1 so no

# 6-3
glossery = {"for": "loop", "variable": "storage", "int": "number"}

for thing in glossery:
    stuff = glossery[thing]
    print(f"a {thing} is used for {stuff}")

