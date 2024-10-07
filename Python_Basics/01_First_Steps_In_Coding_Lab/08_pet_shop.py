dog_food_price = 2.50
cat_food_price = 4
quantity_dog = int(input())
quantity_cat = int(input())
sum_price_dog = quantity_dog * dog_food_price
sum_price_cat = quantity_cat * cat_food_price
sum_overall = sum_price_cat + sum_price_dog
print(f"{sum_overall} lv.")
