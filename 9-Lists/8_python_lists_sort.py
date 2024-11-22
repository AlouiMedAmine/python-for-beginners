################ Python - Sort Lists


######## 1-Sort List Alphanumerically

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort()
print(thislist)

###

thislist = [100, 50, 65, 82, 23]
thislist.sort()
print(thislist)

######## 2-Sort Descending

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse = True)
print(thislist)

###

thislist = [100, 50, 65, 82, 23]
thislist.sort(reverse = True)
print(thislist)

######## 3-Customize Sort Function

def myfunc(n):
  return abs(n - 50)

thislist = [100, 50, 65, 82, 23]
thislist.sort(key = myfunc)
print(thislist)


######## 4-Case Insensitive Sort

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort()
print(thislist)

###

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.sort(key = str.lower)
print(thislist)


######## 5-Reverse Order

thislist = ["banana", "Orange", "Kiwi", "cherry"]
thislist.reverse()
print(thislist)