
############ 1-Getting the Data Type


print("############ 1-Getting the Data Type")
x = 5
print(type(x))

############
x = "Hello World"
print(x," : ",type(x))


x = 20
print(x," : ",type(x))


x = 20.5
print(x," : ",type(x))


x = 1j
print(x," : ",type(x))


x = ["apple", "banana", "cherry"]
print(x," : ",type(x))


x = ("apple", "banana", "cherry")
print(x," : ",type(x))


x = range(6)
print(x," : ",type(x))


x = {"name" : "John", "age" : 36}
print(x," : ",type(x))


x = {"apple", "banana", "cherry"}
print(x," : ",type(x))


x = frozenset({"apple", "banana", "cherry"})
print(x," : ",type(x))


x = True
print(x," : ",type(x))


x = b"Hello"
print(x," : ",type(x))


x = bytearray(5)
print(x," : ",type(x))


x = memoryview(bytes(5))
print(x," : ",type(x))


x = None
print(x," : ",type(x))


############ 2-Setting the Specific Data Type
print()
print("####################################")
print()
print("2-Setting the Specific Data Type")
print()

x = str("Hello World")
print(x," : ",type(x))


x = int(20)
print(x," : ",type(x))


x = float(20.5)
print(x," : ",type(x))

x = complex(1j)
print(x," : ",type(x))


x = list(["apple", "banana", "cherry"])
print(x," : ",type(x))


x = tuple(("apple", "banana", "cherry"))
print(x," : ",type(x))


x = range(6)
print(x," : ",type(x))


x = dict(name= "John", age=36)
print(x," : ",type(x))


x = set(("apple", "banana", "cherry"))
print(x," : ",type(x))


x = frozenset({"apple", "banana", "cherry"})
print(x," : ",type(x))


x = bool(5)
print(x," : ",type(x))


x = bytes(5)
print(x," : ",type(x))


x = bytearray(5)
print(x," : ",type(x))


x = memoryview(bytes(5))
print(x," : ",type(x))


x = None
print(x," : ",type(x))
