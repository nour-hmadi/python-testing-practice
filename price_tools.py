def validate_prices(prices):
    for price in prices:
        if price <= 0:
            ##return ("all prices should be positive")
            ##This just hands back a string, and highest and daily_returns ignore it and carry on calculating. Nothing stops. It must be:
            raise ValueError("All prices must be positive")
            # raise (not return): stops the function and reports the error


def highest(prices):
    validate_prices(prices)
    highest_value = prices[0]
    for price in prices:
        if price > highest_value:
            highest_value = price
    return highest_value
#print(highest([5000, 5050, 5025, 5100, 5000]))


def daily_returns(prices):
    validate_prices(prices)
    the_return = []
    for day in range(1, len(prices)):
        the_return.append(round(((prices[day]/prices[day -1 ] - 1 ) * 100),2))
    return the_return
#print(daily_returns([100, 110, 99]))


def average_price(prices):
    if len(prices)==0:
        raise ValueError("the list is empty")
    else: 
        validate_prices(prices)
        total = 0
        for price in prices:
            total = total + price
        avg = round( total / len(prices),2)    
        return avg

#rint(average_price([]))
#rint(average_price([100, 110, 99]))    # expected: 103.0

