# # # simple_dict = {'1':1,[0,1]:'minhdan'} bad dict 

# # my_dict = {(1,2):'nguyen_minh_dan'}
# # # my_dict = {{'dan': 1223}:'nguyen_minh_dan'}
# # my_dict[1]

# my_dict = {'1':'dan'}
# my_dict['2']

def count_letters(wordlist):
    """ See question description """
    
    ALPHABET = "abcdefghijklmnopqrstuvwxyz"

    letter_count = {}
    for letter in ALPHABET:
        letter_count[letter] = 0
        for character in wordlist:
        	letter_count[character] += 1
    return letter_count
print(count_letters('hello world'))


# monty_quote = "listen strange women lying in ponds distributing swords is no basis for a system of government supreme executive power derives from a mandate from the masses not from some farcical aquatic ceremony"

# monty_words = monty_quote.split(" ")