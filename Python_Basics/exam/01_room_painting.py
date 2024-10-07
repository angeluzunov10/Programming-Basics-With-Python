import math

paint_boxes_count = int(input())
wallpaper_rolls_count = int(input())
gloves_price_per_pair = float(input())
brush_price = float(input())

paint_box_price = 21.50
wallpaper_roll_price = 5.20
gloves_needed = math.ceil(0.35 * wallpaper_rolls_count)
brushes_needed = math.floor(0.48 * paint_boxes_count)

paint_box_total_price = paint_box_price * paint_boxes_count
wallpaper_rolls_total_price = wallpaper_roll_price * wallpaper_rolls_count
gloves_total_price = gloves_price_per_pair * gloves_needed
brushes_total_price = brush_price * brushes_needed

total_spending = paint_box_total_price + wallpaper_rolls_total_price + gloves_total_price + brushes_total_price

delivery_price = total_spending / 15

print(f"This delivery will cost {delivery_price:.2f} lv.")
