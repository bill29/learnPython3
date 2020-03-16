
class superman():
	""" class of superman in the world  """
	origin = 'China'
	def __init__(self, name, sex, power, age):
		self.sex = sex
		self.power = power
		self.age = age
		self.name = name
	def print(self):
		print ('name : {} \n sex : {} \n power : {} \n age :  {} \n Origin : {}'.format(self.name,self.sex,self.power,self.age,self.origin))
	#regular method
	def change_origin(self,country):
		self.origin = country
	#classmethod
	@classmethod
	def change_origin2(cls,country):
		cls.origin = country



#bai 1 , change by class 

# iron_man = superman('minh_dan','men',100,21)
# print(iron_man.origin)
# print(superman.origin)

# print('==============')
# print('Nhan thay duoc su thay doi sau khi thay doi thuoc tinh cua class')

# superman.origin='Japan'
# print(iron_man.origin)
# print(superman.origin)

# print('==============')
# print('Thay doi khi su dung method')

# superman.change_origin(iron_man,'UK')
# print(iron_man.origin)
# print(superman.origin)

# print('Co nghia la khi thay doi method cua doi tuong thi khong anh huong den cac instance khac')
# print('==============')

# superman.origin = 'Indonexia'
# print(iron_man.origin)
# print(superman.origin)

# print('Cap nhat o tren su dung regular method co ve nhu ko thay the duoc toan bo cac doi tuong cua class')
# superman.change_origin2('France')
# print(iron_man.origin)
# print(superman.origin)
# print('neu da su dung regular method thi se ko thay doi duoc doi tuong do')

# print('Neu object do chua su dung regular method: ket qua')
# spiderman = superman('Spiderman','men',70,10)
# # spiderman.change_origin2('Vietnam')
# superman.change_origin2('Vietnam')


# print(spiderman.origin)
# print(superman.origin)

# print('Tai sao lai the boi vi su dung class method nen se thay doi ca class')
# spiderman.change_origin2('Iran')
# print(spiderman.origin)
# print(superman.origin)


# print('Tom lai : classmethod thay doi class , regular method thay doi doi tuong , staticmethod ko lmgi')



#ke thua inhiterance 
 


# class superman_kteam(superman):
# 	def __init__(self,name, sex, power, age, handsome):
# 		self.name = name
# 		self.sex = sex
# 		self.power = power
# 		self.age = age
# 		self.handsome = handsome


class superman_kteam(superman):
		"""docstring for ClassName"""
		def __init__(self, name, sex, power, age, handsome):
			super().__init__(name, sex, power, age)
			self.handsome = handsome
		def print(self):
			super().print()
			print('cap nhat them o lop con')
		def __repr__(self):
			return 'Object'
		def __str__(self):
			return'Object ' + 'Special Method'



kteam = superman_kteam('minhdan','men' ,20,10,10)

print(kteam.__dict__)
kteam.print()


print('=============')
print(kteam)




#over write constructer






