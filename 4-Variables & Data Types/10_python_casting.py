############ 1-Specify a Variable Type


x = int(1)
y = int(2.8)
z = int("3")
print(x)
print(y)
print(z)


############


x = float(1)
y = float(2.8)
z = float("3")
print(x)
print(y)
print(z)



############


x = str("s1")
y = str(2)
z = str(3.0)
print(x)
print(y)
print(z)

###### Notes:

# 1- A string should represent an Integer

x = int("100")

# invalid literal for int() with base 10: 'hello'


y = int('5.0')

# 2-convert the string representation of a floating-point number to integer
# ==> ValueError: invalid literal for int() with base 10: '5.0'

w = int(float('5.0'))
print(w)



