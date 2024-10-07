money_needed = float(input())
money_available = float(input())
total_days = 0
days_in_a_row = 0

while True:
    action = input()
    total_days += 1
    if action == "save":
        saved_money = float(input())
        money_available += saved_money
        if money_needed <= money_available:
            print(f"You saved the money for {total_days} days.")
            break
    elif action == "spend":
        spent_money = float(input())
        days_in_a_row += 1
        if days_in_a_row == 5:
            print("You can't save the money.")
            print(f"{total_days}")
            break



