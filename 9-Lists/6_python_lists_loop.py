################ Python - Loop Lists

######## 1-Loop Through a List

thislist = ["apple", "banana", "cherry"]
for x in thislist:
  print(x)


######## 2-Loop Through the Index Numbers

thislist = ["apple", "banana", "cherry"]
for i in range(len(thislist)):
  print(thislist[i])

######## 3-Using a While Loop

thislist = ["apple", "banana", "cherry"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

######## 4-Looping Using List Comprehension

thislist = ["apple", "banana", "cherry"]
[print(x) for x in thislist]