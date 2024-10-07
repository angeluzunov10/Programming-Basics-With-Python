day_of_week = input()
message_for_print = ""

if day_of_week == "Monday" \
        or day_of_week == "Tuesday" \
        or day_of_week == "Wednesday" \
        or day_of_week == "Thursday" \
        or day_of_week == "Friday":
    message_for_print = "Working day"
elif day_of_week == "Saturday" \
        or day_of_week == "Sunday":
    message_for_print = "Weekend"
else:
    print("Error")
print(message_for_print)

# по-добре по този начин, за да няма 10000 print-ове в кода, така просто променям ст-ста на променливата
