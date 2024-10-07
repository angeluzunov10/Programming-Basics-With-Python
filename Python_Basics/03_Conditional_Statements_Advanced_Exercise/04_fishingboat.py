budget = int(input())
season = input()
fisherman_count = int(input())

rental_price = 0
discount = 0
final_price = 0

if season == "Spring":
    rental_price = 3000

elif season == "Summer" or season == "Autumn":
    rental_price = 4200

elif season == "Winter":
    rental_price = 2600

if fisherman_count <= 6:
    discount = 0.1
    final_price = rental_price * (1 - discount)

elif 7 <= fisherman_count <= 11:
    discount = 0.15
    final_price = rental_price * (1 - discount)

elif fisherman_count >= 12:
    discount = 0.25
    final_price = rental_price * (1 - discount)

if fisherman_count % 2 == 0 \
        and (season == "Spring" or season == "Summer" or season == "Winter"):
    final_price = final_price * (1 - 0.05)

money_needed = 0
money_left = 0

if budget >= final_price:
    money_left = budget - final_price
    print(f"Yes! You have {money_left:.2f} leva left.")
elif budget < final_price:
    money_needed = final_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva.")
