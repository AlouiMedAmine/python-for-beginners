#########               Python Exceptions (Part 1)

######## 1-


####### 2- Exception Handling

#the program will crash and raise an error:

#The try block will generate an exception, because x is not defined:

try:
  print(x)
except:
  print("An exception occurred")


### Example 2:
#This statement will raise an error, because x is not defined:

print(x)


############# 3- Many Exceptions

try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
