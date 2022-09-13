a = 101
b = 100
if a < b:
 print("a is less than b")
 print("a<b")
  
  
# elif
a = 33
b = 30
if b > a:
 print("b is greater than a")
# elif : if the previous condition were not true then try this condition
elif a == b:
 print("b is equal to a")
else: #it catches anything which isn't caught by the precedding conditions
 print("b is less than a")
#else:

# Assignment: take marks from student and print the grade
# marks are 90 -100 ----A grade
# marks are 80 -89  ----B grade
# marks are 70 -79  ----C grade
# marks are 60 -69  ----D grade
# marks are 50 -59  ----E grade
# marks are less than 50 ----fail


marks = int(input("Enter your marks .... (0 -100)"))
print("Your entered marks are:", marks)
if marks >= 90:
 print("you got A grade")
elif marks >= 80:
 print("you got B grade")
elif marks >= 70:
 print("You got C grade")
elif marks >=60:
 print("You got D grade")
elif marks >=50:
 print("You got E grade")
else:
 print("You are fail")

# short hand if

a = 300
b = 76
if a > b: print("a is greater than b")

# short hand for if...else
a = 100
b = 33
print("b is greater than a") if b > a else print("a is greater than b")

# and operator
# and is logical opertor, used to combine conditional statements

a = 200
b = 33
c = 500
if a > b and c > b:
 print("both conditions are true")

# or opertor
a = 200
b = 33
c = 500
if a > b or b > c:
 print("one of the two condition is true")

# nested if
a = 100
if a > 20:
 print("a is greater than 20")
 if a < 50:
  print("a is less than 50")
 else:
  print("but it is not less than 50")


#pass statement
a = 30
b = 40
if b > 30:
    pass
