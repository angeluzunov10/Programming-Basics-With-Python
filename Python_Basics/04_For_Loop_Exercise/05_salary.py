facebook_fee = 150
instagram_fee = 100
reddit_fee = 50
total_fees = 0

opened_tabs_count = int(input())
salary = int(input())

for _ in range(opened_tabs_count):
    tab_name = input()

    if tab_name == "Facebook":
        total_fees += facebook_fee
    if tab_name == "Instagram":
        total_fees += instagram_fee
    if tab_name == "Reddit":
        total_fees += reddit_fee
    if tab_name == "":
        total_fees += 0

salary_left = 0

if salary > total_fees:
    salary_left = salary - total_fees

    print(int(salary_left))
else:
    print("You have lost your salary.")
