tup = (1, 5, 7, 3, 1, 1)
print(tup[:2])
print(tup[1:])
print(tup[1:3])
print(tup)

#index in tuples 
print(tup.count(1))
#the first index == item
print(tup.index(1))

#conversion 

print("========")
list2=[1,2,3,4,5]
tuples_exam = tuple(list2)
#tuples can not change 
#tuples_exam[0]='minh dan'
list3 = list(tuples_exam)
list3[0]='minh_dan'
#print all 
print(tuples_exam, list3 , list2)


# source code in cousera 
"""
Tuple examples.
"""

# Lists and tuples are both sequences
print("Sequences")
print("=========")
lst = [1, 5, 7, 3]
tup = (1, 5, 7, 3)

print(lst, tup)
print(lst[2])
print(tup[2])
print(tup[:2])
print(tup[2:3])

# Tuples are immutable
lst[0] = 9
print(lst)
# tup[0] = 9
# print(tup)

print("")
print("Tuple Methods")
print("=============")

print(tup.index(7))
print(tup.count(4))

print("")
print("Iteration")
print("=========")

for item in tup:
    print(item)

print("")
print("Conversion")
print("==========")

lst2 = [8, 6, 4, 8, 2]
print(lst2)
tup2 = tuple(lst2)
print(tup2)
# tup2[3] = 7
lst3 = list(tup2)
print(lst3)
lst3[2] = 7
print(lst2, tup2, lst3)
