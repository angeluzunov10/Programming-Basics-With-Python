projection_type = input()
column_numbers = int(input())
line_numbers = int(input())
premiere_ticket_price = 12.00
normal_ticket_price = 7.50
discount_ticket_price = 5.00
capacity = column_numbers * line_numbers
income = 0

if projection_type == "Premiere":
    income = capacity * premiere_ticket_price
elif projection_type == "Normal":
    income = capacity * normal_ticket_price
elif projection_type == "Discount":
    income = capacity * discount_ticket_price
print(f"{income:.2f} leva")
