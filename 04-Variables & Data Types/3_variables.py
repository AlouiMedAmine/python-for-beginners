##############       Python Variables

######## 1- Variables

#Variables are containers for storing
# data values.


########2-Creating Variables
print("-------2-Creating Variables-----")

#Example
x = 5
y = "John"
print(x)
print(y)

#Example
x = 4       # x is of type int
print(x)

x = "Sally" # x is now of type str
print(x)


######## 3-Casting
print("-----------3-Casting---------")

x = str(3)    # x will be '3'
y = int(3)    # y will be 3
z = float(3)  # z will be 3.0

print(x)
print(y)
print(z)


######## 4-Get the Type
print("--------4-Get the Type-------")


print(type(x))
print(type(y))
print(type(z))

#Example 2

x = 5
y = "John"
print(type(x))
print(type(y))



######## 5-Single or Double Quotes?
print("----5-Single or Double Quotes?----")

x = "John"
print(type(x))
# is the same as
x = 'John'
print(type(x))



######## 6-Case-Sensitive
print("----- 6-Case-Sensitive-------")

a = 4
A = "Sally"
print(a)
print(A)
#A will not overwrite a