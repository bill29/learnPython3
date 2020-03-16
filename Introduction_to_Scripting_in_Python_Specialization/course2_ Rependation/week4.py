# datafile = open("file_test_read_write.txt","rt")

# data = datafile.read()

# print("Type:", type(data))
# print("Length:", len(data))
# print("=====\n What data :")
# print(data)


data = open("sai.py","rt")

for line in data.readlines():
	print(line)

data.close()
print("========\n =========")
data2 = open("sai.py","rt")

for line in data2:
	print(line)

data2.close()


"""
Iterating over files.
"""

# # Using readlines()
# #  readlines creates a list of strings
# #  that you can iterate over

# datafile1 = open("the_idiot.txt", "rt")

# for line in datafile1.readlines():
#     print(line)

# datafile1.close()

# print("")
# print("================================")
# print("")

# # Direct iteration
# #  This is faster for large files,
# #  as no list is created

# datafile2 = open("the_idiot.txt", "rt")

# for line in datafile2:
#     print(line)

# datafile2.close()


