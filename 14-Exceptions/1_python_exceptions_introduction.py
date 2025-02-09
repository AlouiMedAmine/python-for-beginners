#########                Python Exceptions (Introduction)



######## 1-What are Exceptions in Python?



def divide(x, y):
    try:
       result = x / y
    except ZeroDivisionError:
       print('Division by zero!')
    else:
       print('Result is', result)
    finally:
       print('Executing finally clause')


#divide(2, 0)

divide(2, 2)