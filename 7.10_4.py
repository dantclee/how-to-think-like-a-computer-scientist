with open("newfile_7.10_3.txt", 'r') as infile, open('newfile_7.10_4.txt', 'w') as outfile:
    for line in infile:
        new_line = line[5:]
        outfile.write(new_line)
