nylon_for_sq_meter = 1.50
paint_for_liter = 14.50
thinner_for_liter = 5.0
bags = 0.4

nylon_needed = int(input())
paint_needed = int(input())
thinner_needed = int(input())
hours_needed = int(input())

nylon_total_price = (nylon_needed + 2) * nylon_for_sq_meter  # + 2 са допълнителните 2 кв. найлон, които са по условие, но може да се вкарат като допълнителна променлива , за да е по-разбираемо
paint_total_price = (paint_needed + paint_needed * 0.10) * paint_for_liter # * 0,10  са допълнителните 10 % боя, които са по условие, но може да се вкарат като допълнителна променлива , за да е по-разбираемо
thinner_total_price = thinner_needed * thinner_for_liter

products_price = nylon_total_price + paint_total_price + thinner_total_price + bags
work_price_per_hour = products_price * 0.30

total_payment = products_price + work_price_per_hour * hours_needed

print(total_payment)
