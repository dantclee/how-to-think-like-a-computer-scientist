numbers = [83, 75, 74.9, 70, 69.9, 65, 60, 59.9, 55, 50, 49.9, 45, 44.9, 40, 39.9, 2, 0]
grade = ''
for _ in numbers:
    if _ >= 75:
        grade = 'First'
    elif 70 <= _ < 75:
        grade = 'Upper Second'
    elif 60 <= _ <70:
        grade = 'Second'
    elif 50 <= _ < 60:
        grade = 'Third'
    elif 45 <= _ < 50:
        grade = 'F1 Supp'
    elif 40 <= _ < 45:
        grade = 'F2'
    else:
        grade = 'F3'
    print(_,'\t', grade)
