start = int(input())
final = int(input())
magic_number = int(input())
combinations_count = 0
combination_is_found = False

for first_number in range(start, final + 1):

    for second_number in range(start, final + 1):
        combinations_count += 1

        if first_number + second_number == magic_number:
            combination_is_found = True
            break

    if combination_is_found:
        break

if combination_is_found:
    print(f"Combination N:{combinations_count} ({first_number} + {second_number} = {magic_number})")
else:
    print(f"{combinations_count} combinations - neither equals {magic_number}")
