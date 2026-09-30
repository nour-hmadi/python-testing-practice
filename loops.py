prices = [100, 110, 99]

print("enumerate:")
for day, price in enumerate(prices, start=1):
    print(day, price)

print("range:")
for day in range(1, len(prices)):
    print(day, prices[day], prices[day - 1])