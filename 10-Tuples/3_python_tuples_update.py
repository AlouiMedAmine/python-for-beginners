################  Python - Update Tuples



######## 1-Change Tuple Values

x = ("apple", "banana", "cherry")
y = list(x)
y[1] = "kiwi"
x = tuple(y)
print(x)


######## 2-Add Items

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.append("orange")
thistuple = tuple(y)
print(thistuple)


###Add tuple to a tuple

thistuple = ("apple", "banana", "cherry")
y = ("orange",)
thistuple += y
print(thistuple)


######## 3-Remove Items


#Convert the tuple into a list, remove "apple",
# and convert it back into a tuple:

thistuple = ("apple", "banana", "cherry")
y = list(thistuple)
y.remove("apple")
thistuple = tuple(y)


#The del keyword can delete the tuple completely:
thistuple = ("apple", "banana", "cherry")
del thistuple
print(thistuple) #this will raise an error because the tuple no longer exists