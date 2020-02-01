def dot_product(vec1, vec2):
    product = 0
    for (value1, value2) in zip(vec1, vec2):
        product += value1*value2
    return product

v1 = [1, 2, 1]
v2 = [1, 4, 3]



print(dot_product(v1, v2))
