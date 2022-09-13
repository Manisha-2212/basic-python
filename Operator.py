# program to know keuwords in Python
import keyword
print(keyword.kwlist)
print("Total Number of keywords:",len(keyword.kwlist))

# Program to demonstrate arithmetic operators
x = 100
y = 23
print("Addition of", x , "and", y, "is:", x+y)
x = 100
y = 20
print("x is greater than y?",x>y)
print(x<y)
print(x==y)

# Program to demonstrate logical operators
x = 12
print ("Logical operator OR", (x>5 or x<10))
print ("Logical Operator and",(x>5 and x<10))
print ("Logical operator not",(not(x>5 or x<10)))

# Program to demonstrate identity operators
# is , is not
s1 = 10
s2 = 12
print(s1 is s2)
print(s1 is not s2)
print(id(s1))
print(id(s2))
# Program to demonstrate membership operators

print('ishaa' in 'manisha')  # in operator
print('ishaa' not in 'manisha')  # not in operator
print(12 in[12,10,11])
print(12 not in[12,10,11])


# type casting
# int to string
x = 10
print(type(x))
s = str(x)
print(type(s))

# string to int
y = '2'
print(type(y))
z = int(y)
print(type(z))
