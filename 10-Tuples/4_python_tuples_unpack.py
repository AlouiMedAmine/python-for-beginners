################  Python - Unpack Tuples




######## 1-Unpacking a Tuple

fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits
print(green)
print(yellow)
print(red)



######## 2-Using Asterisk*

fruits = ("apple", "banana", "cherry",
          "strawberry", "raspberry")
(green, yellow, *red) = fruits
print(green)
print(yellow)
print(red)

####


fruits = ("apple", "mango", "papaya",
          "pineapple", "cherry")
(green, *tropic, red) = fruits
print(green)
print(tropic)
print(red)


