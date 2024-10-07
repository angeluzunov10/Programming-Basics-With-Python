space_width = int(input())
space_length = int(input())
space_height = int(input())
total_space = space_width * space_height * space_length
command = ""
free_space = 0
boxes_space = 0
space_needed = 0

while command != "Done":
    command = input()
    if command == "Done":
        break
    boxes_space += int(command)
    if total_space < boxes_space:
        space_needed = boxes_space - total_space
        print(f"No more free space! You need {space_needed} Cubic meters more.")
        break
if total_space >= boxes_space or command == "Done":
    free_space = total_space - boxes_space
    print(f"{free_space} Cubic meters left.")
