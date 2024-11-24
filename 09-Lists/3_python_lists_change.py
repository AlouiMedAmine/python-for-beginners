################  Python - Change List Items



######## 1-Change Item Value

mylist = ["apple", "banana", "cherry"]
mylist[1] = "blackcurrant"
print(mylist)

######## 2-Change a Range of Item Values

mylist = ["apple", "banana", "cherry", "orange", "kiwi", "mango"]
mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist)

########

mylist = ["apple", "banana", "cherry"]
mylist[1:2] = ["blackcurrant", "watermelon"]
print(mylist)

########
mylist = ["apple", "banana", "cherry"]
mylist[1:3] = ["watermelon"]
print(mylist)


######## 3-Insert Items

mylist = ["apple", "banana", "cherry"]
mylist.insert(2, "watermelon")
print(mylist)