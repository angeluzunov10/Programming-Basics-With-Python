# # #Напишете програма за конвертиране на щатски долари (USD) в български лева (BGN). Използвайте фиксиран курс между долар и лев:1 USD = 1.79549 BGN
# USD_TO_BGN = 1.79549
#
# usd = float(input())
# bgn = usd * USD_TO_BGN
#
# print(bgn)

number = int(input())
if number > 0:
    print("It's positive!")
if number == 0:
    print("The number is zero!")
if number < 0:
    print("It's negative!")
