# ============================================
# Exercise 1: Find the highest price (without max())
# print(max(prices))
# ============================================


# Step 1: Create a list with the prices
# A list is written with square brackets [ ],
# with the items separated by commas.
prices = [5000, 5050, 5025, 5100, 5000]
# Step 2: Create a variable "highest" and give it the first price
# Positions in a list start at 0, not 1.
highest = prices[0]
# Check: print the values to make sure they're correct
print("Prices:", prices)
print("Starting highest:", highest)
# Step 3: Go through each price in the list, one by one
# "for price in prices:" means:
#   take the first item and call it "price", run the indented lines,
#   then take the next item, and so on, until the list ends.
# IMPORTANT: the lines inside the loop must be indented (4 spaces).
for price in prices:
    if price > highest:
        highest = price
# Step 5: After the loop ends, "highest" holds the biggest price
print("The highest price is:", highest)

# writing the code again
prices = [3100, 4500, 600, 7800, 10000, 12678, 65739, 65656, 100000]
highest = prices[0]
for price in prices:
    if price > highest:
        highest = price
        ##highest =0, uncomment it to see the assertion error
print("the highest number now is:", highest)
# Step 6: Test: my answer must equal Python's built-in max()
# "assert" checks that something is True.
# If it's True, nothing happens (the test passes).
# If it's False, Python stops and shows an AssertionError (the test fails).
assert highest == max(prices)
print("Test passed: my code gives the same answer as max()")
