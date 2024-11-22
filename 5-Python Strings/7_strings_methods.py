##########    Python - String Methods

########## 1-String Methods

#capitalize()
txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)


#casefold()
txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#count()
txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


#isdigit()
txt = "50800"
x = txt.isdigit()
print(x)

#isupper()
txt = "THIS IS NOW!"
x = txt.isupper()
print(x)


#islower()
txt = "hello world!"
x = txt.islower()
print(x)

#split()
txt = "welcome to the jungle"
x = txt.split()
print(x)

##### string.split(separator, maxsplit)

txt = "hello, my name is Peter, I am 26 years old"
x = txt.split(", ")
print(x)

#####
txt = "apple#banana#cherry#orange"
x = txt.split("#")
print(x)