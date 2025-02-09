################ Python - Copy

# Introduction

#You cannot copy a list simply by typing
#list2 = list1, because: list2 will only
#be a reference to list1, and changes made
#in list1 will automatically also be made
#in list2.



list1 = ["apple", "banana", "cherry"]
list2 = list1
print("list 1 initialy: ", list1)
print("list 2 initialy: ", list2)

list2[1] = "Orange"

print("list 2 : ", list2)
print("list 1 : ", list1)








######## 1-Copy a List

thislist = ["apple", "banana", "cherry"]
mylist = thislist.copy()
print("copy",mylist)

mylist[1] = "Orange"
print("mylist",mylist)
print("Initial list", thislist)










######## 2-Use the list() method(Constructor)


thislist = ["apple", "banana", "cherry"]
mylist = list(thislist)
print("copy",mylist)

mylist[1] = "Orange"
print("after change",mylist)
print("Initial List",thislist)











######## 3-Use the slice Operator


thislist = ["apple", "banana", "cherry"]
mylist = thislist[:]
print("copy",mylist)

mylist[1] = "Orange"
print("after change",mylist)
print("Initial List",thislist)