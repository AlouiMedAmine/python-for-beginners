##########    Python - String Methods


#capitalize()
#Converts the first character to upper case

txt = "hello, and welcome to my world."
x = txt.capitalize()
print (x)
print("txt:   ", txt)

#casefold()
#Converts string into lower case

txt = "Hello, And Welcome To My World!"
x = txt.casefold()
print(x)

#count()
#Returns the number of times a
#specified value occurs in a string


txt = "I love apples, apple are my favorite fruit"
x = txt.count("apple")
print(x)


#The find() method finds the first
# occurrence of the specified value

txt = "Hello, welcome to my world."
x = txt.find("welcome")
print(x)


#The find() method returns -1
# if the value is not found.

txt = "Hello, welcome to my world."
x = txt.find("test")
print(x)

#The index() method is almost the same
# as the find()


txt = "Hello, welcome to my world."
x = txt.index("welcome")
print(x)


#index() method raises an exception
# if the value is not found


txt = "Hello, welcome to my world."
x = txt.index("test")
print(x)


#isdigit()
#Returns True if all characters
# in the string are digits

txt = "5080AA0"
x = txt.isdigit()
print(x)

#isupper()
#Returns True if all characters
# in the string are upper case

txt = "THISaa IS NOW!"
x = txt.isupper()
print(x)


#islower()
#Returns True if all characters
# in the string are lower case

txt = "hello worldAA!"
x = txt.islower()
print(x)


#split()
#	Splits the string at the specified
#	separator, and returns a list

#default separator => "whitespace"

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