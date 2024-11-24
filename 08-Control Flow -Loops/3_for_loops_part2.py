################    Python For Loops(Part 2)


######## 1-Else in For Loop

for x in range(6):
  print(x)
else:
  print("Finally finished!")


#Note: The else block will NOT be executed
#if the loop is stopped by a break statement.


for x in range(6):
  if x == 3: break
  print(x)
else:
  print("Finally finished!")


######## 2-Nested Loops

adj = ["red", "big", "tasty"]
fruits = ["apple", "banana", "cherry"]

for x in adj:
  for y in fruits:
    print(x, y)

##------------

x = [1, 2]
y = [4, 5]

for i in x:
  for j in y:
    print(i, j)


######## 3- The pass Statement

for x in [0, 1, 2]:
  pass

