

my_dict = {'joe':{'Assign1':100, 'Assign2':98, 'Assign3' :100, 'Assign4' :13}
, 'Scott':{'Assign1':100, 'Assign2':98, 'Assign3' :100, 'Assign4' :13}
, 'Scott':{'Assign1':100, 'Assign2':98, 'Assign3' :100, 'Assign4' :13}
, 'John' :{'Assign1':100, 'Assign2':98, 'Assign3' :100, 'Assign4' :13}
}


print(my_dict.get('joe1'))

print(' My Dictionary \n========================================================= ')
format_string = "{:<20}  {:>4}  {:>4}  {:>4}  {:>4} "

header_list = ['name']

for key in my_dict['joe'].keys():
	header_list.append(key)


print('{:<20}  {:>4}  {:>4}  {:>4}  {:>4}'.format(*header_list))


def print_dict(adict):
	for value1 in adict.values():
		print(value1.values())
			




print_dict(my_dict)




NUM_ROWS = 25
NUM_COLS = 25

# construct a matrix
my_matrix = []
for row in range(NUM_ROWS):
    new_row = []
    for col in range(NUM_COLS):
        new_row.append(row * col)
    my_matrix.append(new_row)
 
# print the matrix
#print(my_matrix)
sum1=0
for row in range(NUM_ROWS):
	for col in range(NUM_COLS):
		if row == col:
			sum1 += my_matrix[row][col]
print('sum:' + str(sum1))



NUM_ROWS = 5
NUM_COLS = 9

# construct a matrix
my_matrix = {}
for row in range(NUM_ROWS):
    row_dict = {}
    for col in range(NUM_COLS):
        row_dict[col] = row * col
    my_matrix[row] = row_dict
    
print(my_matrix)
 
# print the matrix
for row in range(NUM_ROWS):
    for col in range(NUM_COLS):
        print(my_matrix[row][col] )
