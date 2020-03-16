
#deo biet gi ve quote , qoute la cai lon gi vay
import csv 
with open('minhdan.csv', newline='') as csvfile:
	filereader = csv.reader(csvfile, delimiter=' ')
	for row in filereader:
		print(row)
		print(','.join(row))

#nghich dai voi dau ngan cach cai xem nao 

print('nghich dai ===== quotechar nay ko anh huong lam nhi ')

with open('minhdan.csv', newline='') as csvfile:
	filereader = csv.reader(csvfile, delimiter = ' ', quotechar="'")
	for row in filereader:
		print(row)
		#print(','.join(row))




print('nghich dai ===== quotechar nay ko anh huong lam nhi ')

with open('minhdan.csv', newline='') as csvfile:
	filereader = csv.reader(csvfile, delimiter = ' ',skipinitialspace=True)
	for row in filereader:
		#print(row)
		print(','.join(row))




print('Neu de cai quote la dau '' thi no se doc duoc va loai bo nhin no dep ')

with open('minhdan.csv', newline='') as csvfile:
	filereader = csv.reader(csvfile, delimiter = ' ',quotechar= "'")
	for row in filereader:
		#print(row)
		print(','.join(row))