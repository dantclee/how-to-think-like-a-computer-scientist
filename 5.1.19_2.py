prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "uack")
    else:
        print(letter + suffix)
