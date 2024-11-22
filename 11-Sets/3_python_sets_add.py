################  Python - Add Set Items


######## 1-Add Items

thisset = {"apple", "banana", "cherry"}
thisset.add("orange")
print(thisset)


######## 2-Add Sets



thisset = {"apple", "banana", "cherry"}
tropical = {"pineapple", "mango", "papaya"}
thisset.update(tropical)
print(thisset)


######## 3-Add Any Iterable


thisset = {"apple", "banana", "cherry"}
mylist = ["kiwi", "orange"]
thisset.update(mylist)
print(thisset)