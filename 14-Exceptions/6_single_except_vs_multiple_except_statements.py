###############    Single except Vs Multiple except ‘Statements’


####### 1: Handling multiple exceptions with a single except statement


"""
________________________________
 Example 1: Handling ZeroDivisionError and ValueError
________________________________
"""


try:
    # Code that may raise different types of exceptions
    x = 10 / 10  # This will raise a ZeroDivisionError : x = 10 / 0
    y = int("10")  # This will raise a ValueError : y = int("a")
except (ZeroDivisionError, ValueError) as e:
    print(f"An error occurred: {e}")


#Explanation: This code will catch both ZeroDivisionError
# (if the user enters 0) and ValueError
# (if the user enters something other than a number).


""" 
________________________________
 Example 2: Handling FileNotFoundError and PermissionError
________________________________
"""

try:
    with open("/home/amine/Desktop/UdemyRepos/python-for-beginners/example2.txt", "r") as file:
        content = file.read()
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"File error: {e}")

#Explanation: This will catch two exceptions related
# to file handling. It will handle cases where the
# file doesn't exist (FileNotFoundError) or if there
# is a permissions issue (PermissionError).

"""
________________________________
 Example 3: Handling TypeError and IndexError in Function Calls
________________________________
"""

def process_data(data):
    try:
        item = data[4]  # May raise IndexError
        result = item + " World !!!"  # May raise TypeError if item is not a string
        print(result)
    except (TypeError, IndexError) as e:
        print(f"Error: {e}")

#process_data([1, 2, 3])
#process_data([1, 2, 3, 4, 5])
process_data([1, 2, 3, 4, "Hello"])

#Explanation: This function might raise either
# a TypeError (if the item is not a string and
# we try to concatenate) or an IndexError
# (if the index 4 does not exist in the list).
# Both are caught in a single except block.

########## 2. Handling multiple exceptions with multiple except statements

"""
________________________________
 Example 1:
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
    print(f"An unexpected error occurred: {e}")





"""
________________________________
 Example 2: (to remember the Key Word: else & finally) 
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


