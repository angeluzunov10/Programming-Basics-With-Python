puzzle = 2.60
speaking_doll = 3.00
fluffy_bear = 4.10
minion = 8.20
truck = 2.00

trip_price = float(input())
puzzle_count = int(input())
speaking_doll_count = int(input())
fluffy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())
total_toys = puzzle_count + speaking_doll_count + fluffy_bear_count + minion_count + truck_count

total_price = (puzzle * puzzle_count) + (speaking_doll * speaking_doll_count) + (fluffy_bear * fluffy_bear_count) + (
            minion * minion_count) + (truck * truck_count)
discount = 0
money_needed = 0
money_left = 0

if total_toys >= 50:
    discount = 0.25 * total_price
    total_price = total_price - discount

shop_rental_price = total_price * 0.1

profit = total_price - shop_rental_price

if profit >= trip_price:
    money_left = profit - trip_price
    print(f"Yes! {money_left:.2f} lv left.")
else:
    money_needed = trip_price - profit
    print(f"Not enough money! {money_needed:.2f} lv needed.")
