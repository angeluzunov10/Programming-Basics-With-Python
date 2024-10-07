numbers_count = int(input())
left_sum = 0
right_sum = 0

for numbers in range(numbers_count * 2): #мислено деля числата на 2 половини, за да знам къде е лява и дясна
    current_number = int(input())
    if numbers < numbers_count:          #тук проверявам дали числата вече въведени горе са под ст-ста която разделя
                                         #двете половини (тая стойност е numbers_count) и ако е под нея, значи е отляво
        left_sum += current_number
    else:
        right_sum += current_number
difference = 0

if left_sum == right_sum:
    print(f"Yes, sum = {right_sum}")
elif right_sum != left_sum:
    difference = abs(left_sum - right_sum)   #abs е абсолютната стойност и тук ни се иска по условие, но не е задължит.
    print(f"No, diff = {difference}")
