age = float(input())
gender = input()
address = ""

if gender == "m":
    if age >= 16:
        address = "Mr."
    else:
        address = "Master"
elif gender == "f":
    if age >= 16:
        address = "Ms."
    else:
        address = "Miss"
print(address)
