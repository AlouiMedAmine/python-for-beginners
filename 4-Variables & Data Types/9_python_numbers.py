############ 1-Python Numbers
print("############ 1-Python Numbers")
x = 1    # int
y = 2.8  # float
z = 1j   # complex

print(type(x))
print(type(y))
print(type(z))

############ 2-Int
print("############ 2-Int")

x = 1
y = 35656222554887711
z = -3255522

print(type(x))
print(type(y))
print(type(z))


############ 3-Float
print("############ 3-Float  Example:1")
x = 1.10
y = 1.0
z = -35.59

print(type(x))
print(type(y))
print(type(z))

############
print("############ 3-Float  Example:2")

x = 35e3
print(x)
y = 12E4
print(y)
z = -87.7e100
print(z)

print(type(x))
print(type(y))
print(type(z))

############ 4-Complex
print("############ 4-Complex")

x = 3+5j
y = 5j
z = -5j

print(type(x))
print(type(y))
print(type(z))

############ 5-Type Conversion
print("############ 5-Type Conversion")

x = 1    # int
y = 2.8  # float
z = 1j   # complex

#convert from int to float:
a = float(x)
print(a)
print(type(a))

#convert from float to int:
b = int(y)
print(b)
print(type(b))

#convert from int to complex:
c = complex(x)
print(type(c))

print(c)

############ 6-Random Number
print("############ 6-Random Number")

import random

print(random.randrange(1, 10))

