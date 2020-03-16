list1= list(range(1,6))*2
list2=list1 + []
#list1 =list(range(123))+list(range(77))
print(list1 == list2)

print(list1)

def strange_sum(numbers):
	sum=0
	for num in numbers:
		if num %3 !=0:
			sum+=num
	return sum 
print(strange_sum(list1))
