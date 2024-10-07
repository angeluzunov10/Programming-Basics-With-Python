student_name = input()
average_degree = 0
total_degree = 0
yearly_degree = 0
grade = 1
exclusions = 0

while grade <= 12:
    yearly_degree = float(input())

    if yearly_degree < 4:
        exclusions += 1
        if exclusions > 1:
            break
        continue

    total_degree += yearly_degree
    grade += 1

if grade <= 12:
    print(f"{student_name} has been excluded at {grade} grade")
else:
    average_degree = total_degree / 12
    print(f"{student_name} graduated. Average grade: {average_degree:.2f}")
