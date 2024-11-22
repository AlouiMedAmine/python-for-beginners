################   Python Dictionaries


######## 1-Loop Through a Dictionary


thisdict =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

#Print all key names
for x in thisdict:
  print(x)


#Print all values
for x in thisdict:
  print(thisdict[x])


#You can also use the values() method
# to return values of a dictionary:

for x in thisdict.values():
  print(x)

#You can use the keys() method
# to return the keys of a dictionary:

for x in thisdict.keys():
  print(x)


#Loop through both keys and values,
#by using the items() method:
for x, y in thisdict.items():
  print(x, y)

