# Напишете програма, която изчислява каква сума ще получите в края на депозитния период при определен лихвен процент.
# Използвайте следната формула:
# сума = депозирана сума  + срок на депозита * ((депозирана сума * годишен лихвен процент ) / 12)

deposit_amount = float(input())
deposit_term = int(input())
annual_interest_rate_percent = float (input())

annual_interest_rate = annual_interest_rate_percent / 100 #превръщам процентите в число

#тук може директно да си напиша annual_interest_rete = float(input()) / 100
#в такъв случай ще ми обълне процентите автоматично

final_amount = deposit_amount + deposit_term * ((deposit_amount * annual_interest_rate) / 12)

print(final_amount)