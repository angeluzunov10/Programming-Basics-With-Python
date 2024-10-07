budget = float(input())
static_actors = int(input())
clothing_price_for_a_static_actor = float(input())
decorations = budget * 0.1

if static_actors > 150:
    clothing_price_for_a_static_actor = clothing_price_for_a_static_actor - (clothing_price_for_a_static_actor * 0.1)

spendings = decorations + (clothing_price_for_a_static_actor * static_actors)
money_left = 0
money_needed = 0

if spendings > budget:
    money_needed = spendings - budget
    print("Not enough money!")
    print(f"Wingard needs {money_needed:.2f} leva more.")
else:
    money_left = budget - spendings
    print("Action!")
    print(f"Wingard starts filming with {money_left:.2f} leva left.")
