###############   Python Identity Operators

#### 1- is
#------------------------------------------------

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)
# because z is the same object as x

print(x is y)
# because x is not the same object as y,
# even if they have the same content

print(x == y)
# this comparison returns True because x is equal to y

## to demonstrate the difference
# betweeen "is" and "==":


#------------------------------------------------
#### 2- is not

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is not z)
# returns False because z is the same object as x

print(x is not y)
# returns True because x is not the same object as y,
# even if they have the same content

print(x != y)
#this comparison returns False because
# x is equal to y


print("Congratulation! you just learn Python Identity Operators !! ")