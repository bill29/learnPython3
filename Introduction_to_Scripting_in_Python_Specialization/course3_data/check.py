"""
Checking for keys in a dictionary.
"""

print("Using 'in'")
print("==========")

mapping = {1: 5, 8: -3, 7: 22, 4: 13, 22: 17}



print('nguyen_minh_dan')
print(mapping[1])
#in use checking in dict ...
# Keys
print(1 in mapping)
print(8 in mapping)

# Values
print(5 in mapping)
print(-3 in mapping)

# Both
print(22 in mapping)

# Neither
print(82 in mapping)

print("")

print("Protecting from Errors")
print("======================")

keys = [8, 14, 22, 25]

#for key in keys:
#    print(key, mapping[key])

for key in keys:
    if key in mapping:
        print(key, mapping[key])
    else:
        print("{} not in mapping".format(key))


print("Issues with Keys")
print("================")
        
# Be careful with what you use as keys!
# If all keys are of the same type, you won't run
#  into these issues
mapping = {4.0: 2, 'a': 3, True: 'true', False: 'false that day'}
print(mapping)

mapping[1] = 7
print(mapping)

mapping[0] = 'false'  # no lai in ra la false , vi 0 tuong ung voi fals
print(mapping)

mapping[4] = 7
print(mapping)

mapping['A'] = 'abc'  #no ko phan biet chu hoa chu thuong
print(mapping)

#python no so sanh su dung khoa , kha la hay va phuc tap day nhi 	