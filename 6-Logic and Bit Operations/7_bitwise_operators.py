##############    Python Bitwise Operators


print(6 & 3)
#The & operator compares each bit and set it to 1
# if both are 1, otherwise it is set to 0:

"""
6 = 0110
3 = 0011
--------------------
2 = 0010
"""

print(6 | 3)
#The | operator compares each bit and set it to 1
# if one or both is 1, otherwise it is set to 0:
"""
6 = 0110
3 = 0011
--------------------
7 = 0111
"""

print(6 ^ 3)
#The ^ operator compares each bit and set it to 1 if only one is 1,
# otherwise (if both are 1 or both are 0) it is set to 0:
"""
6 = 0110
3 = 0011
--------------------
5 = 0101
"""

print(~3)



"""
The ~ operator inverts each bit (0 becomes 1 and 1 becomes 0).

Inverted 3 becomes -4:
 3 = 011
-4 = 100
"""

print(3 << 2)

"""
The << operator inserts the specified number
 of 0's (in this case 2) from the right and 
 let the same amount of leftmost bits fall off:

If you push 00 in from the left:
 3 = 011
becomes
12 = 1100

Note: x << y This is the same as multiplying x by 2**y.

"""


print(8 >> 2)

"""
The >> operator moves each bit the specified
number of times to the right.
Empty holes at the left are filled with 0's.

If you move each bit 2 times to the right, 8 becomes 2:
 8 = 1000
becomes
 2 = 0010
 
Note:  x >> y  his is the same as // x by 2**y
"""