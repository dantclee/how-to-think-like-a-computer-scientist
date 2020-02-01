word_frequency = dict()
fhand = open('Alice_Adventures_large.txt')
for line in fhand:
    lower_string = line.lower().split()
    for word in lower_string:
        if word.isalpha():
            word_frequency[word] = word_frequency.get(word, 0) + 1

words = list(word_frequency.items())
words.sort()

fout = open('alice_words.txt', 'w')
layout = "{0:25}{1:<3}"
fout.write(layout.format('Word','Count') + '\n')
fout.write('='*(25+3+2) + '\n')
for (key, value) in words:
    fout.write(layout.format(key, value) + '\n')
