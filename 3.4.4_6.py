mark = input('Enter exam mark: ')
try:
    fmark = float(mark)
except:
    print('Exam mark must be a number.')
    quit()
grade = ''
if fmark >= 75:
    grade = 'First'
elif 70 <= fmark < 75:
    grade = 'Upper Second'
elif 60 <= fmark <70:
    grade = 'Second'
elif 50 <= fmark < 60:
    grade = 'Third'
elif 45 <= fmark < 50:
    grade = 'F1 Supp'
elif 40 <= fmark < 45:
    grade = 'F2'
else:
    grade = F3
print(grade)
