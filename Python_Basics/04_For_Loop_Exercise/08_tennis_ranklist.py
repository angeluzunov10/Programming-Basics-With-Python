import math
tournaments_count = int(input())
starting_points = int(input())
final_points = starting_points
average_points = 0
percentage_of_tournaments_won = 0
tournaments_won = 0
for _ in range(1, tournaments_count + 1):
    tournament_stage = input()

    if tournament_stage == "W":
        final_points += 2000
        tournaments_won += 1
    elif tournament_stage == "F":
        final_points += 1200
    elif tournament_stage == "SF":
        final_points += 720

average_points = (final_points - starting_points) / tournaments_count
percentage_of_tournaments_won = tournaments_won / tournaments_count * 100

print(f"Final points: {final_points}")
print(f"Average points: {math.floor(average_points)}")
print(f"{percentage_of_tournaments_won:.2f}%")
