import math

serial_name = input()
time_per_episode = int(input())
break_time = int(input())

launch_break_time = break_time / 8
relaxation_time = break_time / 4

total_time_for_activities = relaxation_time + launch_break_time + time_per_episode

time_needed = 0
time_left = 0

if total_time_for_activities <= break_time:
    time_left = break_time - total_time_for_activities
    time_left = math.ceil(time_left)
    print(f"You have enough time to watch {serial_name} and left with {time_left} minutes free time.")
else:
    time_needed = total_time_for_activities - break_time
    time_needed = math.ceil(time_needed)
    print(f"You don't have enough time to watch {serial_name}, you need {time_needed} more minutes.")