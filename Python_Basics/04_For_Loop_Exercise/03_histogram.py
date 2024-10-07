num_count = int(input())
p1_count = 0
p2_count = 0
p3_count = 0
p4_count = 0
p5_count = 0

for numbers in range(num_count):
    current_num = int(input())

    if current_num < 200:
        p1_count += 1
    elif 200 <= current_num <= 399:
        p2_count += 1
    elif 400 <= current_num <= 599:
        p3_count += 1
    elif 600 <= current_num <= 799:
        p4_count += 1
    elif current_num >= 800:
        p5_count += 1

p1_in_percent = p1_count / num_count * 100
p2_in_percent = p2_count / num_count * 100
p3_in_percent = p3_count / num_count * 100
p4_in_percent = p4_count / num_count * 100
p5_in_percent = p5_count / num_count * 100

print(f"{p1_in_percent:.2f}%")
print(f"{p2_in_percent:.2f}%")
print(f"{p3_in_percent:.2f}%")
print(f"{p4_in_percent:.2f}%")
print(f"{p5_in_percent:.2f}%")
