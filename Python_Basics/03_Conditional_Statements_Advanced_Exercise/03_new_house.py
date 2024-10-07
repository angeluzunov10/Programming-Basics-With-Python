flowers_type = input()
flowers_count = int(input())
budget = int(input())
flower_price = 0
discount = 0
final_price = 0

if flowers_type == "Roses":
    price = 5
    if flowers_count > 80:
        discount = 0.1
    final_price = flowers_count * price * (1 - discount)
elif flowers_type == "Dahlias":
    price = 3.80
    if flowers_count > 90:
        discount = 0.15
    final_price = flowers_count * price * (1 - discount)
elif flowers_type == "Tulips":
    price = 2.80
    if flowers_count > 80:
        discount = 0.15
    final_price = flowers_count * price * (1 - discount)
elif flowers_type == "Narcissus":
    price = 3
    if flowers_count < 120:
        discount = -0.15
    final_price = flowers_count * price * (1 - discount)
elif flowers_type == "Gladiolus":
    price = 2.50
    if flowers_count < 80:
        discount = -0.20
    final_price = flowers_count * price * (1 - discount)

money_left = 0
money_needed = 0

if budget >= final_price:
    money_left = budget - final_price
    print(f"Hey, you have a great garden with {flowers_count} {flowers_type} and {money_left:.2f} leva left.")
elif budget < final_price:
    money_needed = final_price - budget
    print(f"Not enough money, you need {money_needed:.2f} leva more.")