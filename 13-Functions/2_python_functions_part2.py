###########  Python Functions (Part2)


####### 1- Number of Arguments

#This function expects 2 arguments,
# and gets 2 arguments:

def my_function(fname, lname):
  print(fname + " " + lname)


my_function("Emil", "Refsnes")


#This function expects 2 arguments,
# but gets only 1:

def my_function(fname, lname):
  print(fname + " " + lname)

my_function("Emil","Emil")








########  2- Arbitrary Arguments, *args
#If the number of arguments is unknown
#add a * before the parameter name:


def my_function(*kids):
  print(kids)
  print("The youngest child is " + kids[2])

my_function("Emil", "Nelson","CR7")


#############

def my_function(*kids):
  print("Kids number are :",  len(kids))

my_function()
my_function("Emil")
my_function("Tobias", "Emil")
my_function("Emil", "Tobias", "Linus")
my_function("Emil", "Tobias", "Linus","Amine")
