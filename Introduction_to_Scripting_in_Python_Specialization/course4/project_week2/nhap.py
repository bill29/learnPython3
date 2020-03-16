BILLION = 1000000000
def suitable_data(list_of_tuple):
	new_list = []
	for a_tuple in list_of_tuple:
		try:
			new_list.append((a_tuple[0],float(a_tuple[1])/BILLION))
		except:
			print('Error !!!')
	return new_list

