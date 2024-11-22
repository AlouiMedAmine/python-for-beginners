################  Python - Access List Items

######## 1-Access Items

mylist = ["apple", "banana", "cherry"]
print(mylist[1])

######## 2-Negative Indexing

mylist2 = ["apple", "banana", "cherry"]
print(mylist2[-1])

######## 3-Range of Indexes

mylist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist3[2:5])


mylist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist3[2:5])


mylist3 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist3[2:])

######## 4-Range of Negative Indexes


mylist4 = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
print(mylist4[-4:-1])


######## 5-Check if Item Exists

mylist4 = ["apple", "banana", "cherry"]
if "apple" in mylist4:
  print("Yes, 'apple' is in the fruits list")