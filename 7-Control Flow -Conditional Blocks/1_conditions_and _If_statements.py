############    If , Elif & Else statements


######### 1-If
a = 33
b = 200
if b > a:
  print("b is greater than a")


######## Indentation
""" 
#If statement, without indentation (will raise an error):

a = 33
b = 200
if b > a:
print("b is greater than a") # you will get an error
"""

######### 2-Elif

a = 33
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")


######### 3-Else

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

########

#You can also have an else without the elif:

a = 200
b = 33
if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")