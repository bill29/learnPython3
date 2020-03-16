contacts = {'Scott Rixner': '1-101-555-1234',
            'Joe Warren': '1-102-555-5678',
            'Jane Doe': '1-103-555-9012'}
def loop_dict(adict):
	for key in adict:
		print adict[key]
loop_dict(contacts)

def loop_dict2(adict,name):
	if name in contacts:
		print('{} has phone number : {}'.format(name,adict[name]))
	else:
		print('Server don\'t have your number of {}'.format(name))
loop_dict2(contacts,'Jane Doe')
loop_dict2(contacts,'Messi')




