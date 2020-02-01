def count_letters(string, letter):
    count = 0
    start = 0
    while start < len(string):
        if string.find(letter, start) != -1:
            count += 1
            start = string.find(letter, start) + 1
        else:
            break
    return count

word = input('Enter a word: ')
letter = input('Enter a letter: ')
print(count_letters(word, letter))
