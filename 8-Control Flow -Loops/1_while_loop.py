###############    Python While Loops


########  1 - The while Loop
print("########  1 - The while Loop")

i = 1
while i < 7:
    print(i)
    i += 1

########  2- The break Statement
print("########  2- The break Statement")

i = 1
while i < 7:
  print(i)
  if i == 3:
    break
  i += 1

########  3 - The continue Statement
print("########  3 - The continue Statement")

i = 0
while i < 7:
    i += 1
    if i == 3:
        continue
    print(i)

########  4-The else Statement
print("########  4-The else Statement")


i = 1
while i < 7:
  print(i)
  i += 1
else:
  print("i is no longer less than 7")