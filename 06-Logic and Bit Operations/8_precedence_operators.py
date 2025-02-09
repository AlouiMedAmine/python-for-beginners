##############    Python Operators Precedence

#The precedence order : starting with the highest precedence

###	1- Parentheses
print((6 + 3) - (6 + 3))

"""
Parenthesis have the highest precedence, and need to be evaluated first.
The calculation above reads 9 - 9 = 0
"""
### 2- Exponentiation

print(100 - 3 ** 3)

"""
Exponentiation has higher precedence than subtraction, and needs to be evaluated first.
The calculation above reads 100 - 27 = 73
"""

##### Note : Bitwise NOT
#	~	Bitwise negation,
#flips the bits of an integer
#num = 5; result = ~5; // result is -6


### 3- Unary plus, unary minus, and bitwise NOT (+x  -x  ~x)

print(100 + ~3)

"""
Bitwise NOT has higher precedence than addition,
and needs to be evaluated first.
The calculation above reads 100 + -4 = 96
"""


### 4- Multiplication, division, floor division, and modulus

print(100 + 5 * 3)

"""
Multiplication has higher precedence than addition, and needs to be evaluated first.
The calculation above reads 100 + 15 = 115
"""

### 5- Addition and subtraction

print(5 + 4 - 7 + 3)

"""
Additions and subtractions have the same precedence, and we need to calculate from left to right.
The calculation above reads:
5 + 4 = 9
9 - 7 = 2
2 + 3 = 5
"""

#6-Bitwise left and right shifts
#7-Bitwise AND
#8-Bitwise XOR
#9-Bitwise OR
#10-Comparisons, identity, and membership operators
#11-Logical NOT
#12-AND
#13-OR

