def add_vectors(vector1, vector2):
    result = []
    for (value1, value2) in zip(vector1, vector2):
        result.append(value1 + value2)
    return result

v1 = [1, 1, 3]
v2 = [2, 3, 999]

print(add_vectors(v1, v2))
