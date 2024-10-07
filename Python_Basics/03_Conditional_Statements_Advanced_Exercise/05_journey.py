budget = float(input())
season = input()
vacation_type = 0
destination = 0
money_spent = 0

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        money_spent = 0.3 * budget
    elif season == "winter":
        money_spent = 0.7 * budget

elif 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        money_spent = 0.4 * budget
    elif season == "winter":
        money_spent = 0.8 * budget

elif budget > 1000:
    destination = "Europe"
    vacation_type = "Hotel"
    money_spent = budget * 0.9

if season == "summer" and not destination == "Europe":
    vacation_type = "Camp"

elif season == "winter":
    vacation_type = "Hotel"

print(f"Somewhere in {destination}")
print(f"{vacation_type} - {money_spent:.2f}")
