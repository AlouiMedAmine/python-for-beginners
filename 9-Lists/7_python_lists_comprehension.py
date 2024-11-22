################ Python - List Comprehension


######## 1-List Comprehension

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = []
for x in fruits:
  if "a" in x:
    newlist.append(x)
print(newlist)

####


fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newlist = [x for x in fruits if "a" in x]
print(newlist)

######## 2-The Syntax

#newlist = [expression for item in iterable if condition == True]

######## A-Condition
newlist = [x for x in fruits if x != "apple"]
print(newlist)

########
newlist = [x for x in fruits]
print(newlist)


####### B-Iterable

newlist = [x for x in range(10)]
print(newlist)

#######
newlist = [x for x in range(10) if x < 5]
print(newlist)


####### C-Expression

#Set the values in the new list to upper case:
newlist = [x.upper() for x in fruits]
print(newlist)

###

#Set all values in the new list to 'hello':
newlist = ['hello' for x in fruits]
print(newlist)

###
#Return "orange" instead of "banana":
newlist = [x if x != "banana" else "orange" for x in fruits]
print(newlist)

