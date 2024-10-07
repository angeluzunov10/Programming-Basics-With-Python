exam_start_hour = int(input())
exam_start_minute = int(input())
arriving_hour = int(input())
arriving_minute = int(input())

minutes_after = 0
hours_after = 0
hours_earlier = 0
minutes_earlier = 0
difference = 0

exam_start_time_as_minutes = exam_start_hour * 60 + exam_start_minute
arriving_time_as_minutes = arriving_hour * 60 + arriving_minute

if arriving_time_as_minutes > exam_start_time_as_minutes:
    print("Late")
    difference = arriving_time_as_minutes - exam_start_time_as_minutes
    if difference < 60:
        minutes_after = arriving_time_as_minutes - exam_start_time_as_minutes
        print(f"{minutes_after} minutes after the start")
    elif difference >= 60:
        hours_after = (arriving_time_as_minutes - exam_start_time_as_minutes) // 60
        minutes_after = (arriving_time_as_minutes - exam_start_time_as_minutes) % 60
        print(f"{hours_after}:{minutes_after:02d} hours after the start")


if arriving_time_as_minutes <= exam_start_time_as_minutes:
    difference = exam_start_time_as_minutes - arriving_time_as_minutes
    if difference <= 30:
        print("On time")
    if not difference == 0:

        if difference < 60:
            minutes_earlier = difference % 60
            print(f"{minutes_earlier} minutes before the start")
        if difference >= 60:
            hours_earlier = difference // 60
            minutes_earlier = difference % 60
            print(f"{hours_earlier}:{minutes_earlier:02d} hours before the start")

    if difference > 30:
        print("Early")
        if difference < 60:
            minutes_earlier = difference % 60
            print(f"{minutes_earlier} minutes before the start")
        if difference >= 60:
            hours_earlier = difference // 60
            minutes_earlier = difference % 60
            print(f"{hours_earlier}:{minutes_earlier:02d} hours before the start")

