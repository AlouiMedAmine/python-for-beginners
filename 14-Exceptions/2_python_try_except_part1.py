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
x = 10
try:
  print(x/0)

except NameError:
  print("Variable x is not defined")

except ZeroDivisionError:
  print('Division by zero!')

except Exception:
  print("Something else went wrong")
