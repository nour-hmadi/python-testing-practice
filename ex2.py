##find the lowest price and the day
prices=[30,40,28,17,2,736,64]
lowest=prices[0]
lowest_day=1
for day, price in enumerate(prices, start =1):
  if price < lowest:
    lowest = price
    lowest_day= day

print("the lowest price is:",  lowest, "and the lowest price day is: ", lowest_day)
# Test: compare with Python's built-in functions
assert lowest == min(prices)
assert lowest_day == prices.index(lowest) + 1
print("All tests passed!")