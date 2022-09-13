
"""
# a. print in Python to produce the
# OUTPUT: Programming***Essentials*** in...Python
"""
print("Programming***Essentials***")


##############################################################################

"""# b. Nursery rhyme of your choice (with proper indentation and newline)
#use \n and \t"""
print("Twinkle, twinkle, little star, \n\tHow I wonder what you are! \n\t\tUp above the world so high, "
      "\n\t\tLike a diamond in the sky. \nTwinkle, twinkle, little star, \n\tHow I wonder what you are!")

##############################################################################

# c.Datatypes in python
# integer
var1 = 10
print("type of variable 1 is:", type(var1))

# string
var2 = 'Manisha'
print("type of variable 2 is:", type(var2))
var3 = 'manisha2212'
print("type of variable 3 is:", type(var3))

# complex
var4 = 3j+2
print("type of variable 4 is:", type(var4))

# Boolean
var5 = True
print("type of variable 5 is:", type(var5))

# ###########################################################################
# Program to demonstrate List data type in Python
empty_list = []
print(empty_list)
print('Type of empty_list is:', type(empty_list))

list1 = [10, 20, 30]
print(list1)
print("list of integer:", list1)
print('type of list is:', type(list1))
print('No. of elements in list1 is:', len(list1))

list2 = [1,2,3,'M']
print('list of mixed data types:', list2)
print('type of list2 is:', type(list2))
print('No. of elements in list2 is:', len(list2))

# ###############################################################
# program to demonstrate dictionary data type in Python
empty_dict = {}
print("this is empty dictionary:", empty_dict)
print("type of empty_dict is:", type(empty_dict))
print('No. of element in empty_dict is:', len(empty_dict))


d1 = {'Name': 'Manisha', 'college': 'VJTI'}
print("The elements of dictionary1 is:", d1)
print("type of d1 is:", type(d1))
print("number of elements are:", len(d1))

# ####################################################
# program to demonstrate dictionary data type in Python
empty_set = set([])
print("The elements in empty_set : ", empty_set)
print("type of empty_set is:", type(empty_set))
print("number of elements in empty_set are: ", len(empty_set))

set1 = set([1, 2, 3, 1])
print("The elements in set1 : ", set1)
print("type of set1 is:", type(set1))
print("number of elements in set1 are: ", len(set1))

set2 = set(['VJTI', 'MUMBAI'])
print("The elements in set2 : ", set2)
print("type of set2 is:", type(set2))
print("number of elements in set2 are: ", len(set2))

set3 = set('MITADT Pune') # set of characters
print("The elements in set3 : ", set3)
print("type of set3 is:", type(set3))
print("number of elements in set3 are: ", len(set3))
