def highest(prices):
    # your Exercise 1 logic goes here
    # (but "return" the result instead of printing it)
    highest_value = prices[0]
    for price in prices:
        if price > highest_value:
            highest_value = price
    return highest_value
print(highest([5000, 5050, 5025, 5100, 5000]))   # should print 5100
print(highest([30, 40, 28, 17, 2, 736, 64]))      # should print 736