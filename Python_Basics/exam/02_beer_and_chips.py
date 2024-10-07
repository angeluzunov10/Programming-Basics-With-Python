import math
fan_name = input()
budget = float(input())
beers_count = int(input())
chips_packs_count = int(input())

beer_price = 1.2
total_beer_price = beer_price * beers_count

chips_pack_price = 0.45 * total_beer_price
total_chips_packs_price = math.ceil(chips_pack_price * chips_packs_count)

total_spending = total_chips_packs_price + total_beer_price

if total_spending <= budget:
    money_left = budget - total_spending
    print(f"{fan_name} bought a snack and has {money_left:.2f} leva left.")
else:
    money_needed = total_spending - budget
    print(f"{fan_name} needs {money_needed:.2f} more leva!")
