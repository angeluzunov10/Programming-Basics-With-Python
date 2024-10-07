food_quantity_in_kg = int(input())
food_quantity_in_grams = food_quantity_in_kg * 1000
command_for_adopt = "Adopted"
command = ""
is_adopted = False
total_food_eaten = 0

while command != command_for_adopt:
    command = input()
    if command == command_for_adopt:
        is_adopted = True
        break
    food_eaten_in_grams = int(command)
    total_food_eaten += food_eaten_in_grams

if total_food_eaten > food_quantity_in_grams:
    food_needed = total_food_eaten - food_quantity_in_grams
    print(f"Food is not enough. You need {food_needed} grams more.")

elif total_food_eaten <= food_quantity_in_grams:
    leftovers = food_quantity_in_grams - total_food_eaten
    print(f"Food is enough! Leftovers: {leftovers} grams.")
