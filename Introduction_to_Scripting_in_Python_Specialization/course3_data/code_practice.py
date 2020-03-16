# # # simple_dict = {'1':1,[0,1]:'minhdan'} bad dict 

# # my_dict = {(1,2):'nguyen_minh_dan'}
# # # my_dict = {{'dan': 1223}:'nguyen_minh_dan'}
# # my_dict[1]

# my_dict = {'1':'dan'}
# my_dict['2']

def get_value(adict):
	for key in adict:
		return adict[key]

def count_letters(word_list):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
    key = []
    for letter in word_list:
    	for i in letter:
    		letter_count[i] += 1
    		if i in key:
    			pass
    		else:
    			key.append(i)
    key.sort()
    letter_sort_count = {}
    for key_sort in key:
    	letter_sort_count[key_sort] = letter_count[key_sort]
    return letter_sort_count


def find_max(a_dict):
	max=0
	for key in a_dict:
		if a_dict[key] >= max:
			max = a_dict[key]
	return max

def find_key(a_dict, value_default):
	list_result = []
	for key in a_dict:
		if a_dict[key] == value_default:
			list_result.append(key)
	return list_result


        
print(count_letters(['dan', 'minhdan']))
monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

monty_words = monty_quote.split(" ")

# print(count_letters(monty_words))


# print(find_max(count_letters(monty_words)))


# max = find_max(count_letters(monty_words))

# print(find_key(count_letters(monty_words), max))


"""
Iterating over dictionaries.
"""

# Mapping from various cities to their country
capitals = {'USA': 'Washington, D.C.',
            'China': 'Beijing',
            'France': 'Paris',
            'England': 'London',
            'Italy': 'Rome',
            'Russia': 'Moscow',
            'Australia': 'Canberra',
            'Peru': 'Lima',
            'Japan': 'Tokyo'}

print("Direct Iteration")
print("================")

for country in capitals:
    print("{}, {}".format(capitals[country], country))

print("")

print("Iteration over Keys")
print("===================")

for country in capitals.keys():
    print("{}, {}".format(capitals[country], country))

print("")

print("Iteration over Values")
print("=====================")

for city in capitals.values():
    print("Capital city: {}".format(city))

print("")

print("Iteration over Items")
print("===================")

for country, city in capitals.items():
    print("{}, {}".format(city, country))

print("")

print("Checking Membership")
print("===================")

print('England' in capitals)
print('Lima' in capitals)

print('Moscow' in capitals.keys())
print('Italy' in capitals.keys())

print('Houston' in capitals.values())
print('Beijing' in capitals.values())









"""
Iterating over dictionaries.
"""

# Mapping from various cities to their country
capitals = {'USA': 'Washington, D.C.',
            'China': 'Beijing',
            'France': 'Paris',
            'England': 'London',
            'Italy': 'Rome',
            'Russia': 'Moscow',
            'Australia': 'Canberra',
            'Peru': 'Lima',
            'Japan': 'Tokyo'}

print("Direct Iteration")
print("================")

for country in capitals:
    print("{}, {}".format(capitals[country], country))

print("")

print("Iteration over Keys")
print("===================")

for country in capitals.keys():
    print("{}, {}".format(capitals[country], country))

print("")

print("Iteration over Values")
print("=====================")

for city in capitals.values():
    print("Capital city: {}".format(city))

print("")

print("Iteration over Items")
print("===================")

for country, city in capitals.items():
    print("{}, {}".format(city, country))

print("")

print("Checking Membership")
print("===================")

print('England' in capitals)
print('Lima' in capitals)

print('Moscow' in capitals.keys())
print('Italy' in capitals.keys())

print('Houston' in capitals.values())
print('Beijing' in capitals.values())







# BAI TOAN MINH GIAI SE DE DANG HON NEU BIET .KEYS , .VALUES 

# KEY , VALUE IN THANHPHO. DICT.items