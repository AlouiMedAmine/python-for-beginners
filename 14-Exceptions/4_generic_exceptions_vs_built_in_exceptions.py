#########               Generic Exceptions Vs Built-in Exceptions (Part 4)


######## 1- Generic Exceptions:
"""
However, using a catch-all exception handler
can also make it harder to debug code, as we
may not know exactly which type of exception
occurred and why."""

#Example 1
try:
    result = 1 / 0
except :
    print("An Exception  occurred")


#Example 2

try:
    result = 10 ** 1000
except:
    print("An Exception  occurred")




########### 2- Built-in Exceptions:

"""
It’s generally recommended to catch specific
exceptions whenever possible, as this makes
the code easier to read , maintain and  get
more information about the error and track down
issues more easily.
"""

#Example 1

try:
    result = 1 / 0  # Division by zero, raises ArithmeticError (ZeroDivisionError)
except ArithmeticError as e:
    print(f"An arithmetic error occurred: {e}")


#Example 2

try:
    result = 1 / 0  # Division by zero, raises ZeroDivisionError
except ZeroDivisionError as e:
    print(f"An zerodivision error occurred: {e}")