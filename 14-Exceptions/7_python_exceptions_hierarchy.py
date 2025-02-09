###############   Python Exceptions Hierarchy


#Example 1: ArithmeticError

try:
    result = 1 / 0  # Division by zero, raises ArithmeticError

except ArithmeticError as e:
    print(f"An arithmetic error occurred: {e}")

#----------------------------------------

#Example 2: FileNotFoundError


try:
    with open("/home/amine/Desktop/UdemyRepos/python-for-beginners/example2.txt", "r") as file:
        content = file.read()
        print(content)
except (FileNotFoundError, PermissionError) as e:
    print(f"File error: {e}")
