################  Python - Join Lists



######## 1-Join Two Lists

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
list3 = list1 + list2
print(list3)


#Append list2 into list1:

list1 = ["a", "b", "c"]
list2 = [1, 2, 3]
for x in list2:
   list1.append(x)
print(list1)




#add list2 at the end of list1

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]
list1.extend(list2)
print(list1)