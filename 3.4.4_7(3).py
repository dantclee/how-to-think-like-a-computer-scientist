n = 25
threshold = 0.001
approximation = n/2 # Start with some or other guess at the answer
while True:
    better = (approximation + n/approximation)/2
    print(better)
    if abs(approximation - better) < threshold:
        print(better)
        break
    approximation = better
