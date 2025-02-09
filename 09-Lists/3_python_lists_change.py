################  Python - Change List Items




######## 1-Change Item Value

mylist = ["apple", "banana", "cherry"]
mylist[1] = "blackcurrant"
print(mylist)














######## 2-Change a Range of Item Values


mylist = ["apple", "banana", "cherry",
          "orange", "kiwi"]
print("N°of items before change : ",len(mylist))
mylist[1:3] = ["blackcurrant", "watermelon"]
print(mylist)
print("After change : " , len(mylist))



#-----------------------------------------------------
# The length of the list will change when the
# number of items inserted does not match the
# number of items replaced.
#-----------------------------------------------------
# Case 1: Insert more items than you replace
# Case 2: Insert less items than you replace









# Case 1: Insert more items than you replace

mylist = ["apple", "banana", "cherry"]
print("N°items before change:",len(mylist))
mylist[1:2] = ["blackcurrant", "watermelon"]
print(mylist)
print("after change: ",len(mylist))









# Case 2: Insert less items than you replace

mylist = ["apple", "banana", "cherry"]
print("Number of items before change : ",len(mylist))
mylist[1:3] = ["watermelon"]
print(mylist)
print("Number of items after change : ",len(mylist))
























######## 3-Insert Items

mylist = ["apple", "banana", "cherry"]
mylist.insert(2, "watermelon")
print(mylist)