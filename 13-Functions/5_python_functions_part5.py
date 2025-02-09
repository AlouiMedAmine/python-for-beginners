

###### 1-Positional-Only Arguments

def my_function(x, /):
  print(x)

my_function(3)

######

def my_function(x):
  print(x)

my_function(x = 3)

########

#But when adding the , / you will
# get  an error if you try
# to send a keyword argument:



def my_function(x, /):
  print(x)

my_function(x = 3)


######### 2- Keyword-Only Arguments

def my_function(*, x):
  print(x)

my_function(x = 3)

########
def my_function(x):
  print(x)

my_function(3)

#########
#But with the *, you will get
#an error if you try to send
#a positional argument:



def my_function(*, x):
  print(x)

my_function(3)

######### 3-Combine Positional-Only and Keyword-Only

#Note:
#Any argument before the / , are positional-only,
# and any argument after the *, are keyword-only.

def my_function(a, b, /, *, c, d):
  print(a + b + c + d)

my_function(5, 6, c = 7, d = 8)


