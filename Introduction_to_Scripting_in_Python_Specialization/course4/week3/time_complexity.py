#toan tu in o day khong phai la toan tu for ma la in
import time
test_list = []
test_dict = {}
test_set = {1}
for i in range(100):
	test_list.append(i)
	test_dict[i]=True
	test_set.add(i)
test_tuple = tuple(test_dict)
# test measure effciency of code
# start_time1 = time.time()
# for i in test_list:
# 	if i in test_list:
# 		pass
# end_time1 = time.time()
# print('"in" operation iteracters through entire list to check membership ' + str(end_time1 - start_time1))

# start_time2 = time.time()
# for j in test_list:
# 	if j in test_dict:
# 		pass
# end_time2 = time.time()
# print('"in" operation iteracters through entire dict to check membership ' + str(end_time2 - start_time2))

import operator

def measure_time(list_or_dict_or_set_or_tuples):
	start_time = time.time()
	if i in list_or_dict_or_set_or_tuples:
		pass
	end_time = time.time()
	return end_time - start_time

list_time = {}

list_time['dict']= measure_time(test_dict)
list_time['list']= measure_time(test_list)
list_time['tuple']= measure_time(test_tuple)
list_time['set']= measure_time(test_set)


# sorted_list_time = sorted(list_time.items(),key =operator.itemgetter(1))
sorted_list_time = sorted(list_time.items(), key = lambda item: item[1] )

print(sorted_list_time)