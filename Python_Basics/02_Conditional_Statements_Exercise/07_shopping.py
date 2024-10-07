budget = float(input())
video_chipset_count = int(input())
processors_count = int(input())
ram_memory_count = int(input())

video_chipset_price_per_one = 250
video_chipset_price_total = video_chipset_price_per_one * video_chipset_count

processors_price_per_one = video_chipset_price_total * 0.35
processors_price_total = processors_price_per_one * processors_count

ram_memory_price_per_one = video_chipset_price_total * 0.1
ram_memory_price_total = ram_memory_price_per_one * ram_memory_count

total_spending_price = video_chipset_price_total + processors_price_total + ram_memory_price_total

money_needed = 0
money_left = 0

if video_chipset_count > processors_count:
    total_spending_price = total_spending_price - (total_spending_price * 0.15)

if budget >= total_spending_price:
    money_left = budget - total_spending_price
    print(f"You have {money_left:.2f} leva left!")
else:
    money_needed = total_spending_price - budget
    print(f"Not enough money! You need {money_needed:.2f} leva more!")