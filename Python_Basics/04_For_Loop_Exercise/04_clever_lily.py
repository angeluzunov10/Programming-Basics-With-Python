lilly_age = int(input())
washing_machine_price = float(input())
toy_price = int(input())
brothers_theft = 0
money_from_spending = 0
money_from_sold_toys = 0
total_money = 0

for age in range(1, lilly_age + 1):
    if age % 2 == 0:
        if lilly_age >= 2:
            money_from_spending += age / 2 * 10
            brothers_theft += 1
    else:
        money_from_sold_toys += toy_price


total_money = money_from_sold_toys + money_from_spending - brothers_theft

money_left = 0
money_needed = 0

if total_money >= washing_machine_price:
    money_left = total_money - washing_machine_price

    print(f"Yes! {money_left:.2f}")
else:
    money_needed = washing_machine_price - total_money

    print(f"No! {money_needed:.2f}")
