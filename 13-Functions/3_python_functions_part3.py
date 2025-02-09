###########  Python Functions (Part3)



####### 1- Keyword Arguments

#Note : This way the order of the
# arguments does not matter.


def my_function(child3, child2, child1):
  print("The youngest child is " + child1)

my_function(child1 = "Emil", child2 = "Tobias", child3 = "CR7")



####### 2- Arbitrary Keyword Arguments, **kwargs

#If the number of keyword arguments
#is unknown, add a double ** before
#the parameter name:


def my_function(**kid):
  print("His last name is " + kid["lname"])

my_function(fname = "Tobias", lname = "Refsnes")