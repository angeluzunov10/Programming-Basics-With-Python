searched_book = input()
books_count = 0

current_command = input()

while current_command != "No More Books":
    current_book = current_command

    if current_book == searched_book:
        break

    books_count += 1
    current_command = input()

if current_command != "No More Books":
    print(f"You checked {books_count} books and found it.")
else:
    print("The book you search is not here!")
    print(f"You checked {books_count} books.")
