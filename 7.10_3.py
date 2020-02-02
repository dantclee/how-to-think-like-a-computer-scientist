line_num = 1

with open("Alice_Adventures_large.txt", 'r') as infile, open('newfile_7.10_3.txt', 'w') as outfile:
    for line in infile:
        new_line = ('{0:4}' + ' ' + line).format(line_num)
        outfile.write(new_line)
        line_num += 1
