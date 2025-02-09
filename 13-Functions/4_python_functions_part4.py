###########  Python Functions (Part3)


######## 1- Default Parameter Value

def my_function(country = "Norway"):
  print("I am from " + country)

my_function("Sweden")
my_function("India")
my_function()
my_function("Brazil")



######### 2-Passing a List as an Argument

def my_function(food):
  for x in food:
    print(x)


fruits = ["apple", "banana", "cherry"]

my_function(fruits)
