def add_vectors(vector1, vector2):
    result = vector1
    for (index, value) in enumerate (vector2):
        result[index] += value
    return result

v1 = [1, 1]
v2 = [2, 3]

print(add_vectors(v1, v2))
