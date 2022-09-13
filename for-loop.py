# for loop
# syntax
"""for var_name in sequence(string, list, dict, set, tuple):
    print(var_name)"""
# iterate a string
s = 'Manisha'
for i in s:
    print(i)

# iterate a list

list1 = ['Amos','Om','Praj']
for name in list1:
    print(name)

# break statement in for loop
list1 = ['Amos','Om','Praj','Saad','Abhi']
for name in list1:
    print(name)
    if name == 'Om':
        break

# write a program in python to print names from list which starts with A
# list1 = ['Amos','Om','Praj','Saad','Abhi']

list1 = ['Amos','Om','Praj','Saad','Abhi']
for name in list1:
    if name.startswith('A'):
        print(name)
# range function
for i in range(6):
    print(i)

for i in range(1,11):
    for j in range(1,11):
        print(i*j,"\t")

# range function with step value
# by default step value is 1
for i in range(10, 1, -2):
    print(i)

# else in for loop
for i in range(1,5):
    print(i)
else:
    print("for loop completed...")
