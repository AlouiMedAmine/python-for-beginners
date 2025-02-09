##########   Python - Format - Strings

######### 1-String Format

age = 36
txt = "My name is John, I am " + age
print(txt)

######### 2-F-Strings

age = 36
txt = f"My name is John, I am {age}"
print(txt)

######### 3-Placeholders and Modifiers

#A placeholder can contain variables, operations,
# functions, and modifiers to format the value.

###### a-variable

price = 59
txt = f"The price is {price} dollars"
print(txt)

###### b-modifier
#A modifier is included by adding a colon : followed
# by a legal formatting type, like .2f


price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

###### c-operation

txt = f"The price is {20 * 59} dollars"
print(txt)

###### d-functions

def sum():
    return 20 + 59

txt = f"The price is {sum()} dollars"
print(txt)