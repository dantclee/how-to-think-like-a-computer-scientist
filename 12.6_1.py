def redposint():
    number = input('Enter a positive integer: ')
    try:
        integer_number = int(number)
    except:
        print('Please enter an integer')
    else:
        print('You have entered {0}'.format(integer_number))
redposint()
