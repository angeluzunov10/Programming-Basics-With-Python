figure_type = input()
area = 0
if figure_type == "square":
    side_a = float(input())
    area = side_a * side_a
    #print(f"{square_area:.3f}")
elif figure_type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
    #print(f"{rectangle_area:.3f}")
elif figure_type == "circle":
    radius = float(input())
    from math import pi
    area = pi * radius ** 2
    #print(f"{circle_area:.3f}")
elif figure_type == "triangle":
    triangle_side = float(input())
    height = float(input())
    area = (triangle_side * height) / 2
    #print(f"{triangle_area:.3f}")
print(f"{area:.3f}")
