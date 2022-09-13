# tuples
# ordered and unchangable
# empty tuple
t1 = ()
print(t1)
t1 = (1,2)
print(t1)
t1 = (1, "a",2,'b')
print(t1)
print(type(t1))

#comma seprated values datatype is tuple
t1 = 1,2,3
print(type(t1))

# allow duplicate
t1 = (1,2,3)
print(t1)

#length of tuple
print("number of elemets in tuple :",len(t1))

# accessing element
print(t1[0])

# negative indexing
print(t1[-2])

# slicing
print(t1[0:2])
print(t1[:])
print(t1[:-1])

# update element of tuple
t1 = ("apple","banana","kiwi", "grapes", "watermelon")
# step1: convert tuple into list
l1 = list(t1)
print(l1)
# step2: update list
l1[1] = "mango"
print(l1)
# step3: convert list into tuple
t1 = tuple(l1)
print(t1)

# check if itenm exists in tuple
t1 = ("apple","banana","kiwi", "grapes", "watermelon")
if 'banana' in t1:
    print("banana is present")
else:
    print("banana is not present")

print(dir(list))
# insert mango in t1
t1 = ("apple","banana","kiwi", "grapes", "watermelon")
print(t1)
l1 = list(t1) #step1
l1.append("mango") #step2
t1 = tuple(l1) #step3
print(t1)

#memory required is more in list
t1 = (1)
l1 =[1]
print("size of tuple is:", t1.__sizeof__())
print("size of list is:",l1.__sizeof__())
