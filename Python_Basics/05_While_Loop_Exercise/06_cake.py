cake_length = int(input())
cake_width = int(input())
total_dimensions = cake_width * cake_length
command_for_stop = "STOP"
command = ""
pieces_left = 0
total_brought_pieces = 0

while command != command_for_stop:
    command = input()
    if command == command_for_stop:
        print(f"{pieces_left} pieces are left.")
        break
    pieces_brought = int(command)
    total_brought_pieces += pieces_brought
    if total_brought_pieces > total_dimensions:
        pieces_needed = total_brought_pieces - total_dimensions
        print(f"No more cake left! You need {pieces_needed} pieces more.")
        break
    pieces_left = total_dimensions - total_brought_pieces

if total_brought_pieces < total_dimensions and not command == command_for_stop:
    print(f"{pieces_left} pieces are left.")
