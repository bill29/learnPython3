def sum_of_two_last_item_append_to_list(alist):
	for i in range(20):
		alist.append(alist[-1] + alist[-2])
		print(alist)
fib = [0,1]
sum_of_two_last_item_append_to_list(fib)

print(fib[-1])
