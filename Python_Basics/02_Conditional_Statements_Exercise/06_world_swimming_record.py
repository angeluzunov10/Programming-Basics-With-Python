record = float(input())
length = float(input())
time_per_meter = float(input())
delay = (length // 15) * 12.5  # тук отбелязваме закъснението, /
# тоест колкото пъти се събира 15 в метрите, умножаваме по 12,5,/
# за да добавим разликата която му се натрупва

ivan_time = (length * time_per_meter) + delay
time_needed = 0

if ivan_time < record:
    print(f"Yes, he succeeded! The new world record is {ivan_time:.2f} seconds.")
else:
    time_needed = ivan_time - record
    print(f"No, he failed! He was {time_needed:.2f} seconds slower.")
