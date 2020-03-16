file = open("test1.txt", "rt")
list1 = []
for line in file.readlines():
	if line[-1]=='\n':
		line = line[:-1]
	list1.append(line)
file.close()



line =[]

print(len(line))

print(list1)

# print(list1)