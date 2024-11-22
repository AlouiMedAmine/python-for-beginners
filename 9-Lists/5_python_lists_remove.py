################ Python - Remove List Items

######## 1-Remove Specified Item

thislist = ["apple", "banana", "cherry"]
thislist.remove("banana")
print(thislist)

###

thislist = ["apple", "banana", "cherry", "banana", "kiwi"]
thislist.remove("banana")
print(thislist)

######## 2- Remove Specified Index

thislist = ["apple", "banana", "cherry"]
thislist.pop(1)
print(thislist)

###

thislist = ["apple", "banana", "cherry"]
thislist.pop()
print(thislist)

###

thislist = ["apple", "banana", "cherry"]
del thislist[0]
print(thislist)

###

thislist = ["apple", "banana", "cherry"]
del thislist

######## 3-Clear the List

thislist = ["apple", "banana", "cherry"]
thislist.clear()
print(thislist)