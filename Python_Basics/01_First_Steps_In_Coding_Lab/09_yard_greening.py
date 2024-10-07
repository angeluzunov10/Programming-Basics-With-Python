one_square_price = 7.61
all_squares = float(input())
all_squares_price = all_squares * one_square_price
discount = all_squares_price * 0.18
total_price = all_squares_price - discount
print(f"The final price is: {total_price} lv.")
print(f"The discount is: {discount} lv.")
