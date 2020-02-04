import time

nterms = int(input('Terms start from 0.  Enter term: '))
#nterms = 35
if nterms == 0:
    print('{0}th term is 0'.format(nterms))
elif nterms == 1:
    print('{0}st term is 1'.format(nterms))
else:
    two_term_b4 = 0
    one_term_b4 = 1
    count = 1
    while count < nterms:
        sum = two_term_b4 + one_term_b4
        two_term_b4 = one_term_b4
        one_term_b4 = sum
        count += 1
    print('{0}th term is'.format(nterms), sum)
print(time.process_time())
