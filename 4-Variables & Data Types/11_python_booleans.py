############ 1-Boolean Values

print(10 > 9)
print(10 == 9)
print(10 < 9)


a = 200
b = 33

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")



############ 2-Evaluate Values and Variables

print(bool("Hello"))
print(bool(15))


############ 3-Most Values are True


print(bool("abc"))
print(bool(123))
print(bool(["apple", "cherry", "banana"]))


############ 4-Some Values are False

print(bool(False))
print(bool(None))
print(bool(0))
print(bool(""))
print(bool(()))
print(bool([]))
print(bool({}))


class myclass():
  def __len__(self):
    return 0

myobj = myclass()
print(bool(myobj))


############ 5-Functions can Return a Boolean

#You can create functions that returns a Boolean Value:

def myFunction() :
  return True

print(myFunction())

#########

# Print "YES!" if the function returns True, otherwise print "NO!":
def myFunction() :
  return True

if myFunction():
  print("YES!")
else:
  print("NO!")

######### isinstance() function, which can be used to determine if an object is of a certain data type:

x = 200
print(isinstance(x, int))

print("Congratulation ! you just learn Python Boolean !!! ")




