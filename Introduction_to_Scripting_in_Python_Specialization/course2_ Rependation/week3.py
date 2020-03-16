# list can append adding item to list 
# list can insert item to list(index)
#list can extend lst2 to lst1 vao phia last 
	# append list2 vao list1 se thanh ra thanh phan cuoi la 1 list
"""
list can removing item 
1 pop
remove item in last list
"""
my_list = list(range(10))

my_list.append(10)
my_list.insert(0,'minh_dan')
dan_list = ['minh_toai']

my_list.extend(dan_list)
print(dan_list)
print(dan_list)
print('Print list after extend list:')
print(my_list)

my_list.pop()
print(my_list)

my_list.remove('minh_dan')
print(my_list)


