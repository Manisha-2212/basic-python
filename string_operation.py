# program to demonstrate different string functions
s = 'Manisha'
s1 = "Manisha"
print(s is s1)
print("id of s",id(s))
print("id of s1",id(s1))
s = 'Manisha'
print(len(s))


# indexing
print(s[3])

# slicing
# varible_name[start_index:end_index]
print(s[2:5])
print(s[1:])
print(s[:6])
print(s[:])

# negative slicing
s = 'Manisha'
print(s[2:-1])


# string concatenation
s1 = 'MIT'
s2 = 'ADT'
s3 = s1 + " " + s2
print("Hi,", s3)


# string functions
s ='hello, how are you?'
s1 = s.upper()
print(s.upper())
print(s1.isupper())
print(s1.lower())
print(s.capitalize())
print(s.title())

s =' manisha '
print("original string",s)
print("length of string before applying strip function",len(s))
print("strip:",s.strip())
print("length of string after applying strip function",len(s.strip()))
print("lstrip:", s.lstrip())
print("length of string after applying lstrip function",len(s.lstrip()))
print("rstrip:", s.rstrip())
print("length of string after applying rstrip function",len(s.rstrip()))

s ='#manisha#'
print("original string",s)
print("length of string before applying strip function",len(s))
print("strip:",s.strip('#'))
print("length of string after applying strip function",len(s.strip()))
print("lstrip:", s.lstrip('#'))
print("length of string after applying lstrip function",len(s.lstrip()))
print("rstrip:", s.rstrip('#'))
print("length of string after applying rstrip function",len(s.rstrip()))

s = 'MITU21IBCS0001'
print(s.strip('MITU'))

s = "I like mango, mango and only mango"
s1 = s.replace("mango", "apple",2)
print(s1)

age = 36
name = 'Manisha'
print("My name is {} and my age is {}".format(name, age ))

age = 36
name = 'Manisha'
print("My name is {1} and my age is {0}".format(age, name ))

s = 'how are you?'
txt = s.startswith('Hello')
print (txt)

s = 'how are you'
txt = s.endswith('?')
print (txt)

s = "abaa"
print(s)
s1 = s[::-1]
print(s1)
txt = s.find('hello')
print(txt)
#print(s[::-1])
if s==s1:
    print(s, " is palindrome string")
else:
    print("not palindrome")

#print(s.count('a'))
s = 'abc'
help(s.find)
#print('manisha', sep = '  ', end = 'G')
s ='Manisha'
print(s.count('ana'))

s = 'MaNisha'
print("s string is:", s)
s1 = s.swapcase()
print("s1 string is:", s1)
s2 = s1.swapcase()
print("s2 string is:",s2)

s = 'Manisha'
print(s.isalpha())
s = '12sdff'
print(s.isalnum())
s = '1234'
print(s.isdigit())
s = '   '
print(s.isspace())

s = 'Manisha'
k = s.split()
print(k)
print(type(k))

s = 'My name is: Manisha: My age is 36'
k = s.split(":")
print(k)
print(type(k))

print(':'.join(k))
print(''.join(s))
