month = input()
nights = int(input())

studio = 0
apartment = 0
studio_discount = 0
apartment_discount = 0
final_price_for_studio = 0
final_price_for_apartment = 0

if month == "May" or month == "October":
    studio = 50
    if 7 < nights <= 14:
        studio_discount = 0.05
    elif nights > 14:
        studio_discount = 0.3

    final_price_for_studio = nights * studio * (1 - studio_discount)

    apartment = 65
    if nights > 14:
        apartment_discount = 0.1

    final_price_for_apartment = nights * apartment * (1 - apartment_discount)

elif month == "June" or month == "September":
    studio = 75.20
    if nights > 14:
        studio_discount = 0.2

    final_price_for_studio = nights * studio * (1 - studio_discount)

    apartment = 68.70

    if nights > 14:
        apartment_discount = 0.1

    final_price_for_apartment = nights * apartment * (1 - apartment_discount)

elif month == "July" or month == "August":
    studio = 76
    final_price_for_studio = nights * studio * (1 - studio_discount)

    apartment = 77

    if nights > 14:
        apartment_discount = 0.1

    final_price_for_apartment = nights * apartment * (1 - apartment_discount)

print(f"Apartment: {final_price_for_apartment:.2f} lv.")
print(f"Studio: {final_price_for_studio:.2f} lv.")

