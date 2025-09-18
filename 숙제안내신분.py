student_numbers = []
for _ in range(28):
    num = int(input())
    student_numbers.append(num)

all_students = set(range(1,31))
good_students = set(student_numbers)
bad_students = list(all_students - good_students)
bad_students.sort()
for i in bad_students:
    print(i)