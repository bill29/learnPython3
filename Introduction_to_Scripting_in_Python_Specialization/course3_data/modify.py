print('Dictionary Lookup')
print('=================')

my_dict ={'one':'minhdan', 'two':'nguyen_tinh', 'three':'tri_hoan'}
print(my_dict['one'])

#when find dict have a key , i should use get

print(my_dict.get('one'))

print(my_dict.get(1))

print(my_dict.get(1,'if dont have 1 please print that sentence'))

# dict nay thuc su hay...


#modify 
my_dict['one'] = 'Can_Khanh_Linh' # if old dict have that key , they upd
print(my_dict['one'])
