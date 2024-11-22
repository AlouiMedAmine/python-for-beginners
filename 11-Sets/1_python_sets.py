################  Python Sets


######## 1-Set

#Create a Set:

thisset = {"apple", "banana", "cherry"}
print(thisset)


######## 2-Set Items

####C-Duplicates Not Allowed


thisset = {"apple", "banana", "cherry", "apple"}
print(thisset)


#### True and 1 is considered the same value:


thisset = {"apple", "banana", "cherry", True, 1, 2}
print(thisset)


##### False and 0 is considered the same value:


thisset = {"apple", "banana", "cherry", False, True, 0}
print(thisset)


######## 3-Get the Length of a Set


thisset = {"apple", "banana", "cherry"}
print(len(thisset))


######## 4-Set Items - Data Types

set1 = {"apple", "banana", "cherry"}
set2 = {1, 5, 7, 9, 3}
set3 = {True, False, False}

#### A set with strings, integers and boolean values:

set1 = {"abc", 34, True, 40, "male"}


######## type()

myset = {"apple", "banana", "cherry"}
print(type(myset))

######## The set() Constructor


# note the double round-brackets

thisset = set(("apple", "banana", "cherry"))
print(thisset)

