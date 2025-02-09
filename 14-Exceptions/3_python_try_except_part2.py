#########               Python Exceptions (Part 2)


######## 1-Else


try:
  print("Hello")
except:
  print("Something went wrong")
else:
  print("Nothing went wrong")


############# 2- Finally


try:
  print(x)
except:
  print("Something went wrong")
finally:
  print("The 'try except' is finished")


####### Example 2

try:

  f = open("demofile.txt")
  try:
    f.write("Lorum Ipsum")
  except:
    print("Something went wrong when writing to the file")
  finally:
    f.close()

except:
  print("Something went wrong when opening the file")


########### 3-Raise an exception
#The raise keyword is used to raise an exception.


x = -1

if x < 0:
  raise Exception("Sorry, no numbers below zero")

####### Example 2

###Raise a TypeError if x is not an integer:

x = "hello"

if not type(x) is int:
  raise TypeError("Only integers are allowed")




