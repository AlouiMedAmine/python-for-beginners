################  Python - Access Tuple Items


######## 1-Access Tuple Items

thistuple = ("apple", "banana", "cherry")
print(thistuple[1])



######## 2-Negative Indexing

thistuple = ("apple", "banana", "cherry")
print(thistuple[-1])


######## 3-Range of Indexes

thistuple = ("apple", "banana", "cherry", "orange",
             "kiwi",  "melon", "mango")
print(thistuple[2:5])


####

thistuple = ("apple", "banana", "cherry", "orange",
             "kiwi", "melon", "mango")
print(thistuple[:4])


#####

thistuple = ("apple", "banana", "cherry", "orange",
             "kiwi", "melon", "mango")
print(thistuple[2:])

######## 4-Range of Negative Indexes


thistuple = ("apple", "banana", "cherry", "orange",
             "kiwi", "melon", "mango")
print(thistuple[-4:-1])


######## 5-Check if Item Exists

thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
  print("Yes, 'apple' is in the fruits tuple")