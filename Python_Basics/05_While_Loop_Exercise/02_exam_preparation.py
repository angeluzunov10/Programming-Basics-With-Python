command_for_end = "Enough"
not_good_threshold = 4
current_not_good_grades_count = 0
total_grades = 0
problems_count = 0
last_problem_name = ""

not_good_grades = int(input())

while True:
    command = input()
    if command == command_for_end:
        break

    last_problem_name = command
    problem_grade = int(input())
    problems_count += 1
    total_grades += problem_grade

    if problem_grade <= not_good_threshold:
        current_not_good_grades_count += 1

        if current_not_good_grades_count >= not_good_grades:
            break
average_grade = total_grades / problems_count

if command == command_for_end:
    print(f"Average grade: {average_grade:.2f}")
    print(f"Number of problems: {problems_count}")
    print(f"Last problem: {last_problem_name}")
else:
    print(f"You need a break, {current_not_good_grades_count} poor grades.")
