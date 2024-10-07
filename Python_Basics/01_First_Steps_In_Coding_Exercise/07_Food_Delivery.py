chicken_menu = 10.35
fish_menu = 12.40
vegetarian_menu = 8.15

chicken_amount = chicken_menu * int(input())
fish_amount = fish_menu * int(input())
vegetarian_amount = vegetarian_menu * int(input())

food_price = chicken_amount + fish_amount + vegetarian_amount
dessert = food_price * 0.2
delivery = 2.50

total_price = food_price + dessert + delivery

print(total_price)