################  Python Dictionaries


######## 1-Dictionary

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict)

#As of New Python version 3.7 , 3.8 ,....
#### so getting the first key / value in the dictionary
#can be done as

first_key = list(thisdict)[0]
print(first_key)

first_val = list(thisdict.values())[0]
print(first_val)


######## 2-Dictionary Items

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])

######## C-Duplicates Not Allowed

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964,
  "year": 2020
}
print(thisdict)


######## 3-Dictionary Length

print(len(thisdict))


######## 4-Dictionary Items - Data Types

thisdict = {
  "brand": "Ford",
  "electric": False,
  "year": 1964,
  "colors": ["red", "white", "blue"]
}


########  type()

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(type(thisdict))



########  The dict() Constructor

thisdict = dict(name = "John", age = 36, country = "Norway")
print(thisdict)