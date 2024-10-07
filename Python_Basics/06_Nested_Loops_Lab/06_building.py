floors_count = int(input())
rooms_per_floor = int(input())
room_type = ""
for current_floor in range(floors_count, 0, - 1):
    if current_floor == floors_count:
        room_type = "L"
    elif current_floor % 2 == 0:
        room_type = "O"
    else:
        room_type = "A"

    for current_room in range(rooms_per_floor):
        print(f"{room_type}{current_floor}{current_room}", end = " ")
    print()
