
#1-Python Indentation


#Example

if 5 > 2:
    print("Five is greater than two!")


###### Syntax Error:
'''

if 5 > 2:
print("Five is greater than two!")

'''
######

'''
if 5 > 2:
        print("Five is greater than two!")
if 5 > 2:
          print("Five is greater than two!")
'''

###### Syntax Error:

#You have to use the same number of spaces
# in the same block of code,
# otherwise Python will give you an error:

'''
if 5 > 2:
    print("Five is greater than two!")
     print("Five is greater than two!")
        
'''