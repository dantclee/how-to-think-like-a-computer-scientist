letter_frequency = dict()
string = input('Enter a string: ')
lower_string = string.lower().replace(' ','')
for letter in lower_string:
    letter_frequency[letter] = letter_frequency.get(letter, 0) + 1
letter_items = list(letter_frequency.items())
letter_items.sort()
for (key, value) in letter_items:
    print(key, value)
