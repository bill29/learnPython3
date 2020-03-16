string = 'M 2,3 L 5,6 M 7,8'


boundary_data = 'M 405.63598,251.83 L 409.24698,251.415 L 409.67498,255.323 L 409.71998,255.692 L 409.02198,256.291 L 408.85498,256.306 L 408.35898,256.26 L 408.07398,256.183 L 407.69998,256.094 L 407.52498,256.085 L 407.33998,256.094 L 407.08298,256.179 L 407.02098,256.233 L 406.63198,257.211 L 405.74898,257.292 L 405.19098,251.879 L 405.63598,251.83'
boundary_data = boundary_data.replace('z', '')
boundary_data = boundary_data.replace('M', 'L')

#print(boundary_data)
boundary_list = boundary_data.split('L')[1:]

list_tuple = []
for entry in boundary_list:
	(x, y) = entry.split(',')
	print(x,y)
	print(type(x))


#print(boundary_list)
