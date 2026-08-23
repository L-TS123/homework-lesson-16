# 1. Ask the user for four grades
grades = {}
grades['math'] = int(input('math grade: '))
grades['english'] = int(input('english grade: '))
grades['literature'] = int(input('literature grade: '))
grades['python'] = int(input('python grade: '))
# 2. Add the average
sum(grades.values())
avg =(sum(grades.values())/len(grades))
grades['average'] = avg
# 3. Add the highest and the lowest:
max(grades.values())
min(grades.values())
grades['max grade'] = max(grades.values())
grades['min grade'] = min(grades.values())
# 4. The literature exam was cancelled
del grades['literature']
print(grades)