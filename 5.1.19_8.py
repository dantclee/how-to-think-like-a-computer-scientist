def reverse(string):
    print(string, end ='')
    index = -1
    while index >= -len(string):
        letter = string[index]
        print(letter, end='')
        index -= 1
    return ''

string = input('Enter a string: ')
print(reverse(string))
