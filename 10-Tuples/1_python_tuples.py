################  Python Tuples


######## 1-Tuple

thistuple = ("apple", "banana", "cherry")
print(thistuple)

######## 2-Tuple Items

#Allow Duplicates
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)

######## 3-Tuple Length

thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


######## 4-Create Tuple With One Item
thistuple = ("apple",)
print(type(thistuple))

#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


######## 5-Tuple Items - Data Types

tuple1 = ("apple", "banana", "cherry")
tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)

#A tuple can contain different data types
tuple1 = ("abc", 34, True, 40, "male")

########  6-type()

mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


######## 7-The tuple() Constructor

thistuple = tuple(("apple", "banana", "cherry")) # note the double round-brackets
print(thistuple)