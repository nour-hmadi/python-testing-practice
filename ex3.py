##Returns the largest one-day fall in price. If the price never falls, it returns 0.
##biggest_drop([100, 95, 97, 80])   # → 17
##biggest_drop([1, 2, 3])           # → 0
##checks the list not empty
##calculates the diff between each two consecutive days
##finds the max diff and retrun it
def validate_prices(prices):
    if len(prices) == 0:
        raise ValueError("the list is empty")
    for price in prices:
        if price <=0:
            raise ValueError("the list should only have positive numbers")


def biggest_drop(prices):
    validate_prices(prices)
    if len(prices) == 1:
        raise ValueError("Not enough prices: at least 2 are needed")
    diff = []
    for day in range (0,len(prices)-1):
        diff.append(prices[day] - prices[day +1])
    larg_fall=max(diff)
    if larg_fall<0:
        diff.append(0)
    return max(diff)

#biggest_drop([100, 95, 97, 80])
print(biggest_drop([1, 2, 3]))   # expected: 0
print(biggest_drop([100,95,97,80]))
#  print(biggest_drop([100]))

def count_up_days(prices):
    validate_prices(prices)
    count=0
    for day in range (0, len(prices) -1):
        if prices[day + 1 ] - prices[day]>0:
            count=count+1
    return count

print(count_up_days([1,2,3,4,5,4,3,2,1,1,1,1]))
#should return 4


def count_currencies(trades):
   count={}
   for currency in trades:
        if  currency.upper() in count:
            count[currency.upper()]=count[currency.upper()] + 1
        else:
            count[currency.upper()]=1
   return count
    
print(count_currencies(["USD", "LBP", "USD"]))
#print(count_currencies({"USD", "LBP", "USD"}))
print({"USD", "LBP", "USD"})