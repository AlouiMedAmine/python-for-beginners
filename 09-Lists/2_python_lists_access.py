################  Python - Access List Items



######## 1-Access Items

mylist = ["apple", "banana", "cherry"]
print(mylist[0])
print(mylist[1])
print(mylist[2])














######## 2-Negative Indexing

mylist2 = ["apple", "banana", "cherry"]
print(mylist2[-1])
print(mylist[-2])
print(mylist[-3])












######## 3-Range of Indexes


#mylist3[start_value:end_value]
# always the end_value is excluded



mylist3 = ["apple", "banana", "cherry",
           "orange", "kiwi", "melon", "mango"]

print(mylist3[2:5])









#delete the start value



mylist3 = ["apple", "banana", "cherry",
           "orange","kiwi", "melon", "mango"]


print(mylist3[:5])











#Delete the end value

mylist3 = ["apple", "banana", "cherry", "orange",
           "kiwi", "melon", "mango"]
print(mylist3[2:])




print(mylist3[:])









######## 4-Range of Negative Indexes


mylist4 = ["apple", "banana", "cherry", "orange",
           "kiwi", "melon", "mango"]
print(mylist4[-len(mylist4):-1])










######## 5-Check if Item Exists

mylist4 = ["apple", "banana", "cherry"]
if "apple" in mylist4:
  print("Yes, 'apple' is in the fruits list")











