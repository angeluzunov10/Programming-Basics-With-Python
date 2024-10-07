pens = 5.80
markers = 7.20
chemical_per_liter = 1.20

pens_count = int(input())
markers_count = int(input())
chemical_liters_count = int(input())
discount = int(input()) / 100

price = pens * pens_count + markers * markers_count + chemical_per_liter * chemical_liters_count
price_with_discount = price - (price * discount)

print (price_with_discount)
