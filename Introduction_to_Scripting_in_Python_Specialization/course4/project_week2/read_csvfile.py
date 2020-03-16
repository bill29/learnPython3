import csv
def read_csv_as_list_dict(filename, separator, quote):
	"""
	Inputs
	filename	- name of csv file
	separator	- character that separator fields
	quote 		- character used to optionaly quote fields 
	Output: Return a list of dictionaries where each item in the list corresponds to row in csv
			The Dictionaries in the list map the field names to the field values for that row 
	"""
	table = []
	with open(filename,"rt",newline='') as csvfile:
		csv_reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
		for row in csv_reader:
			table.append(row)
	return table
def read_csv_as_nested_dict(filename,keyfield, separator, quote):
	table = {}
	with open(filename, "rt", newline='') as csvfile:
		csv_reader = csv.DictReader(csvfile, delimiter=separator, quotechar=quote)
		for row in csv_reader:
			rowid = row[keyfield]
			table[rowid] = row
	return table
def read_csv_as_nested_list(filename, separator, quote):
	print('nguyen minh dan')
	with open(filename, "rt", newline='') as csvfile:
		table = []
		csv_reader = csv.reader(csvfile, delimiter=separator, quotechar=quote)
		print(type(csv_reader))
		#print(csv_reader.__doc__)
		for row in csv_reader:
			table.append(row)
	return table
def test_read_csv_file():
	"""
	print result of read function
	"""
	print(read_csv_as_list_dict('dan_test_gdp.csv', ',','"'))
	print(type(read_csv_as_list_dict('dan_test_gdp.csv', ',', '"')))
	print(read_csv_as_nested_list('dan_test_gdp.csv', ',', '"'))
	print(read_csv_as_nested_dict('dan_test_gdp.csv','Country Name' ,',', '"'))
#test_read_csv_file()


