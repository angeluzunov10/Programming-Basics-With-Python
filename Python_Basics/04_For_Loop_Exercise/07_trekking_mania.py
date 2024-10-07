number_of_groups = int(input())
total_people = 0

people_for_musala = 0
people_for_montblanc = 0
people_for_kilimanjaro = 0
people_for_k2 = 0
people_for_everest = 0

percent_for_musala = 0
percent_for_montblanc = 0
percent_for_kilimanjaro = 0
percent_for_k2 = 0
percent_for_everest = 0

for _ in range(number_of_groups):
    number_of_people = int(input())
    total_people += number_of_people

    if number_of_people <= 5:
        people_for_musala += number_of_people
    elif 6 <= number_of_people <= 12:
        people_for_montblanc += number_of_people
    elif 13 <= number_of_people <= 25:
        people_for_kilimanjaro += number_of_people
    elif 26 <= number_of_people <= 40:
        people_for_k2 += number_of_people
    elif number_of_people >= 41:
        people_for_everest += number_of_people

percent_for_musala = people_for_musala / total_people * 100
percent_for_montblanc = people_for_montblanc / total_people * 100
percent_for_kilimanjaro = people_for_kilimanjaro / total_people * 100
percent_for_k2 = people_for_k2 / total_people * 100
percent_for_everest = people_for_everest / total_people * 100

print(f"{percent_for_musala:.2f}%")
print(f"{percent_for_montblanc:.2f}%")
print(f"{percent_for_kilimanjaro:.2f}%")
print(f"{percent_for_k2:.2f}%")
print(f"{percent_for_everest:.2f}%")
