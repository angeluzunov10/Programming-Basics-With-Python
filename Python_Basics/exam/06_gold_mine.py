locations_count = int(input())

for _ in range(1, locations_count + 1):
    expected_average_production_of_gold_per_day = float(input())
    number_of_days_in_current_location = int(input())
    total_production = 0
    for day in range(1, number_of_days_in_current_location + 1):
        production_for_day = float(input())
        total_production += production_for_day
        average_production_for_gold_per_day = total_production / number_of_days_in_current_location

    if average_production_for_gold_per_day >= expected_average_production_of_gold_per_day:
        print(f"Good job! Average gold per day: {average_production_for_gold_per_day:.2f}.")
    else:
        production_needed = expected_average_production_of_gold_per_day - average_production_for_gold_per_day
        print(f"You need {production_needed:.2f} gold.")
