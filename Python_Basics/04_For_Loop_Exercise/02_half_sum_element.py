import sys
numbers_count = int(input())
max_number = - sys.maxsize
numbers_sum = 0

for numbers in range(numbers_count):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    numbers_sum += current_number

rest_sum = numbers_sum - max_number    #тук вадим от цялата сума нашето число, защото то трябва да е извън останалите

if max_number == rest_sum:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    print("No")
    print(f"Diff = {abs(max_number - rest_sum)}")
