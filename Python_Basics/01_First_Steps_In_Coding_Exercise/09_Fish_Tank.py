tank_length = int(input())
tank_width = int(input())
tank_height = int(input())
other_stuffs = float(input()) / 100

tank_volume = (tank_length * tank_width * tank_height) * 0.001 # 0,001 защото 1 литър = 1 куб.дм

water_volume = tank_volume - (tank_volume * other_stuffs)

print(water_volume)