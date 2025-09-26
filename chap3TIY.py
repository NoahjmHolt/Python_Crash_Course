
# section 1 Lists

# 3-1
'''
friends = ["ME", "Tanner", "Riley", "Owen"]
print(friends[1])
print(friends[3])
print(friends)

# 3-2
for friend in friends:
    print("Hello, " + friend)
'''

'''
# 3-3
newList = ["stuff", "things", 'fiz', 'buz']

# 3-4
historical = ["Abe", "Joe", "Jeff"]
for famous in historical:
    print("Come to dinner this Friday, " + famous)

# 3-5
print('\njoe cant come\n')
historical[1] = 'joeseph'
for famous in historical:
    print("Come to dinner this Friday, " + famous)

# 3-6
print('\nThere is a bigger table, who else should come?\n')

historical.insert(0, 'Thomas')
historical.insert(2, 'levi')
historical.append('Tyler')
for famous in historical:
    print("Come to dinner this Friday, " + famous)

# 3-7
print('\nTable wont make it in time\n')

listSize = len(historical)
# print(listSize)   Was using size of and it wasnt giving the len of the list so had to switch things up
while listSize > 2:
    historical.pop()
    listSize = len(historical)

for famous in historical:
    print("Come to dinner this Friday, " + famous)
    
'''

# 3-8
worldWonders = ['Brazil', 'Netherlands', 'Ireland', 'Spain', 'Andora']

print(sorted(worldWonders))
print(worldWonders)
worldWonders.reverse()
print(worldWonders)
worldWonders.reverse()
print(worldWonders)

