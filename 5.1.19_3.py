def count_letters(string, letter):
    count = 0
    for _ in string:
        if _ == letter:
            count += 1
    return count



word = input('Enter a word: ')
letter = input('Enter a letter: ')
print(count_letters(word, letter))
