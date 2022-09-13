# List
# ordered, changable and allow duplicate values
l1 = ["apple", "banana", "cherry"]
print(l1)
print(len(l1))

#list support indexing
print(l1[1])
print(l1[2])

# it support negative indexing
print(l1[-3])

#it support range of index
print(l1[0:2])
print(l1[-1:])

# change list item
l1[1] = 'kiwi'
print(l1)

# change range of item values
l1[0:2] = ['watermelon','grapes']
print(l1)

# append items in the list
l1.append("apple")
print(l1)

# insert at specific index
l1.insert(1,'kiwi')
print(l1)

#remove specific item from list
# value based
"""l1.remove('kiwi')
print(l1)"""

# remove speific item from list
# index based
l1.pop(5)
print(l1)

#list comrehension
# it offers shorter syntax
# syntax
# new_list = [expression for item in ierable if condition == True]
# Without list comprehension
l1 = ["apple", "banana", "cherry","kiwi", "watermelon", "grapes" ]
empty_list = []
for i in l1:
    if "a" in i:
        empty_list.append(i)
print(empty_list)

# list comprehension
print("with list comprehension")
l1 = ["apple", "banana", "cherry","kiwi", "watermelon", "grapes" ]
new_list = [x for x in l1 if "a" in x]
print(new_list)

# create a new list with numbers greater than 10
# using list comprehension
num = [10, 1, 2,45, 34, 56, 3]
#output = [45, 34, 56]
output = [x for x in num if x>10]
print(output)



# create a new list with only even numbers
# using list comprehension

num = [10, 1, 2,45, 34, 56, 3]
#output = [10, 2, 34, 56]
even = [x for x in num if x%2==0]
print(even)

#build-in functions of list
l1 = ["apple", "banana", "cherry","kiwi", "watermelon", "grapes" ]
print(l1)
l1.reverse()
print(l1)
print(l1[::-1])

# sort function
l1 = ["apple", "banana", "cherry","kiwi", "watermelon", "grapes" ]
# bydefault it will sort items in ascending order
l1.sort()
print("Ascending order",l1)
# to sort list in descending order
l1.sort(reverse=True) 
print("Descending order",l1)

l1 = ["apple", "Banana", "Cherry","kiwi", "watermelon", "grapes" ]
# bydefault it will sort items in ascending order
l1.sort(key=str.lower)
print("Ascending order",l1)
# to sort list in descending order
l1.sort(reverse = True,key = str.lower)
print("Descending order",l1)

# copy a list
l1 = [12, 1, 3, 5, 3, 2,13, 45]
l2 =l1.copy()
print(l2)

# join function
l1 = [12, 1, 3, 5, 3, 2,13, 45]
l2 = ['a', 'b', 'c']
l3 = l2+l1
print(l3)
print(l1.count(3))
