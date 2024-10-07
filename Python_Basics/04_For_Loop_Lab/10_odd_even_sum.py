numbers_count = int(input())
odd_sum = 0
even_sum = 0
difference = 0

for numbers in range(1, numbers_count + 1):
    current_number = int(input())
    if numbers % 2 == 0:            #проверката е от for а не в current_number
        odd_sum += current_number
    else:
        even_sum += current_number

if odd_sum == even_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")
else:
    difference = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {difference}")
