###############    Built-in Exceptions


# Example 1: UnboundLocalError

def example_function():
    print(x)  # Trying to print x before it's assigned
    x = 10
    print(x)

example_function()

"""
The error occurs because x is being used
in the print(x) statement before it is
given a value. Python treats x as a local
variable inside the function. 
So when you try to reference it before
it’s assigned, Python throws an UnboundLocalError.
"""

def example_function():
    x = 10
    print(x)  # Now x is defined


example_function()

#---------------------------------

#Example 2: ArithmeticError
try:
    result = 1 / 0  # Division by zero, raises ArithmeticError
except ArithmeticError as e:
    print(f"An arithmetic error occurred: {e}")

#---------------------------------

#Example 3: ZeroDivisionError

try:
    result = 1 / 0  # Division by zero, raises ZeroDivisionError
except ZeroDivisionError as e:
    print(f"An zerodivision error occurred: {e}")

#----------------------------------

#Example 4: AssertionError

def divide(a, b):
    # Assert that b is not zero
    assert b != 0, "Division by zero is not allowed!"
    return a / b

# This will work
#print(divide(10, 2))

# This will raise an AssertionError
print(divide(10, 0))

"""
In this example, the assert statement 
checks that b is not zero. If b is zero,
the code will raise an AssertionError 
with the message 
"Division by zero is not allowed!".
"""



#------------------------------


