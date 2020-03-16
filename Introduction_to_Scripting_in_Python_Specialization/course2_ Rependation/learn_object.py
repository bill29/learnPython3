lst1 = [7, 3, 3]
lst2 = [7, 3, 3]

# [] la mot doi tuong no duoc luu trong bo nho 
# lst1 , lst2 chi la cai ten duoc tham chieu den

print(lst1, lst2)

# That ra la no trong khac nhau day 
lst1[0]='minh_dan'

print(lst1, lst2)


# >>>> Nhu vay day la 2 object khac nhau duoc da o 2 vung bo nho


minhdan = list(range(10))
minhthuong = minhdan

minhthuong[0]='minh_toai'

print(minhdan, minhthuong) 

# in ra

khanh_linh = list(minhdan)

khanh_linh[0] = 'minh_dan'

print(minhdan,khanh_linh)

#giai thich thi day la khanh linh tham chieu den doi tuong khac
#doi tuong nay coppy cua minh dan ko phai minh dan



"""
Giai thich ham vi sao no thay doi khi su dung ham
ly do la mot cai ten o ngoai global
mot cai ten o trong local variable 
tuy nhien no cung tham chieu den mot cai
"""
def change_list(alist):
	alist.insert(0,'entrepreneur')
list_test = list(range(10))
print(list_test)
change_list(list_test)
print(list_test)

print("=========")
print(list_test[1:-1])
# arr[min,max]
# from min to max (not contain max)
#khi ma noi den doi tuong la python no hieu 
#viec luu tru cua no , dia chi cua no trong 
# o nho hehe

tuples = ([1,2],)
print(tuples)

# co the biey dien dieu nay bang cach 
# su dung python tuto
