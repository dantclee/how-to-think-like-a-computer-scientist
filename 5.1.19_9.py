def remove_letter(letter, string):
    for character in string:
        if character == letter:
            continue
        else:
            print(character, end ='')
    return ''

string = input('Enter a string: ')
letter = input('Enter a letter: ')
print(remove_letter(letter,string))
