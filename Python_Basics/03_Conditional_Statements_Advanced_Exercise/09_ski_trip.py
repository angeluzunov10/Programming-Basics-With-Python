days = int(input())
room_type = input()
grade = input()

room_for_one_person = 18
apartment = 25
president_apartment = 35
discount = 0
final_price = 0
nights = days - 1

if room_type == "room for one person":
    final_price = nights * room_for_one_person

elif room_type == "apartment":

    if days < 10:
        discount = 0.3
    elif 10 <= days <= 15:
        discount = 0.35
    elif days > 15:
        discount = 0.5

    final_price = nights * apartment * (1 - discount)

elif room_type == "president apartment":

    if days < 10:
        discount = 0.1
    elif 10 <= days <= 15:
        discount = 0.15
    elif days > 15:
        discount = 0.2

    final_price = nights * president_apartment * (1 - discount)

if grade == "positive":
    final_price = final_price + (final_price * 0.25)
elif grade == "negative":
    final_price = final_price - (final_price * 0.1)

print(f"{final_price:.2f}")
