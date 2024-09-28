grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}

students_list = sorted(list(students))
grades_list = []

for i in grades:
    j = sum(i) / len(i)
    grades_list.append(j)

grades_dict = dict(zip(students_list, grades_list))

print(grades_dict)
