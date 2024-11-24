################    Python For Loops(Part 1)


######## 1-Python For Loops

fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

######## 2-Looping Through a String

for x in "banana":
  print(x)


######## 3-The break Statement


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)
  if x == "banana":
    break



fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    break
  print(x)



######## 4-The continue Statement


fruits = ["apple", "banana", "cherry"]
for x in fruits:
  if x == "banana":
    continue
  print(x)


######## 5-The range() Function


for x in range(6):
  print(x)

# range(6) is not the values of 0 to 6,
# but the values 0 to 5.

##### Using the start parameter:


for x in range(2, 6):
  print(x)


##### Increment the sequence with 3 (default is 1):

for x in range(2, 30, 3):
  print(x)