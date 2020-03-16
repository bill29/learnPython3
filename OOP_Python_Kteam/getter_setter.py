class name:
	def __init__(self, ho, ten):
		self.ho = ho
		self.ten = ten
		# self.email = ho + ten + '@gmail.com'
	@property
	def thongtin(self):
		return '{} {}'.format(self.ho,self.ten )
	@property
	def email(self):
		return self.ho + self.ten + '@gmail.com'
	@email.setter
	def email(self,list):
		# self.email = ho + ten + '@gmail.com'
		self.ho = list[0]
		self.ten = list[1]

minhdan = name('minh', 'dan')
print(minhdan.ho)
print(minhdan.ten)
print(minhdan.email)
print(minhdan.thongtin)

print('======')
minhdan.ho='neymar'
minhdan.ten = 'jr'
#getter
print(minhdan.email)
print(minhdan.thongtin)


print('=========')
minhdan.email = ['nguyen','minhdan']

print(minhdan.email)


