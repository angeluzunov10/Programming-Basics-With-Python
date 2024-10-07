pastry = input()
pastry_count = int(input())
day_of_december = int(input())
cake_price = 0
souffle_price = 0
baklava_price = 0
if day_of_december <= 15:
    cake_price = 24
    souffle_price = 6.66
    baklava_price = 12.60
elif day_of_december > 15:
    cake_price = 28.70
    souffle_price = 9.80
    baklava_price = 16.98

# total_cake_price = pastry_count * cake_price
# total_souffle_price = pastry_count * souffle_price
# total_baklava_price = pastry_count * baklava_price
total_price = 0
if pastry == "Cake":
    total_price = pastry_count * cake_price
elif pastry == "Souffle":
    total_price = pastry_count * souffle_price
elif pastry == "Baklava":
    total_price = pastry_count * baklava_price

discount = 0
total_price_with_discount = total_price

if day_of_december <= 22 and 100 <= total_price <= 200:
    discount = 0.15
    total_price_with_discount = total_price - total_price * discount
elif day_of_december <= 22 and total_price > 200:
    discount = 0.25
    total_price_with_discount = total_price - total_price * discount

if day_of_december <= 15:
    total_price_with_discount = total_price_with_discount - total_price_with_discount * 0.1
    
print(f"{total_price_with_discount:.2f}")
