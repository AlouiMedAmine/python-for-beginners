##########           Exceptions Hierarchy For Multiple Except Statements

"""
________________________________
 Example 1:
________________________________
"""


try:
    x = int(input("Enter a number: "))
    result = 10 / x + "test"

except Exception as e:
    print(f"An unexpected error occurred: {e}")

except ValueError as e:
    print(f"Oops! That was not a valid number. {e}")

except ZeroDivisionError as e:
    print(f"Error: You can't divide by zero. {e}")









"""
________________________________
 Example 2: (General except(default except))
________________________________
"""

try:
    x = int(input("Enter a number: "))
    result = 10 / x




except ValueError:
    print("Oops! That was not a valid number.")
except ZeroDivisionError:
    print("Error: You can't divide by zero.")
except :
    print("Default except")








"""
________________________________
 Example 3: (to remember the Key Word: else & finally) 
________________________________
"""

try:
    x = int(input("Enter a number: "))
    result = 10 / x

except ValueError:
    print("Oops! That was not a valid number.")
except ZeroDivisionError:
    print("Error: You can't divide by zero.")
except:
    print("Default except")

else:
    print(f"Result is {result}")
finally:
    print("Execution complete.")


