####### exercise 1 #######
### Write second_largest(nums), which returns the second largest distinct value in a list. If there are fewer than two distinct values, raise a ValueError. econd_largest([4, 9, 2, 9, 7]) → 7 ###
### my answer for exercise 1 ###
def validate_list(nums):
    if len(nums) < 2:
        raise ValueError("2 numbers should be in the list")
    distinct_values=0
    for i in range(0,len(nums)):
        if nums[0]!=nums[i]:
            distinct_values=1
    if distinct_values==0:
        raise ValueError("at least 2 distinct values should be in the list") 
    return(nums)
print(validate_list([2,1,1,1,1]))
def second_largest(nums):
    validate_list(nums)
    nums.sort(reverse=True)
    largest_dropped=[]
    for i in range (0,len(nums)):
        if nums[0]!=nums[i]:
            largest_dropped.append(nums[i])
    largest_dropped.sort(reverse=True)
    return largest_dropped[0]
### my answer for exercise 1 done ###
### correction for exercise 1 ###
def second_largest_corrected(nums):
    distinct = sorted(set(nums), reverse=True)
    if len(distinct) < 2:
        raise ValueError("Need at least two distinct values")
    return distinct[1]
### correction for exercise 1 done ###
### set(nums) removes duplicates: [4, 9, 2, 9, 7] becomes {4, 9, 2, 7}.
### sorted(..., reverse=True) gives a new list, largest first: [9, 7, 4, 2].
### The second largest is simply position 1. One check covers both error cases.
####### exercise 1 done #######

####### exercise 2 #######
###Write is_palindrome(text), which returns True if the text reads the same forwards and backwards, ignoring spaces and capital letters.###\
### my answer for exercise 2 ###
def is_palindrome_corrected(text):
    text=text.replace(" ","")
    text=text.lower()
    n = len(text)
    text_palindrome=True
    for i in range (0, n):
        if text[i]  != text[ n-1-i]:
            text_palindrome = False    
    return (  text_palindrome)
### my answer for exercise 2 done ###
###correcton for exercise 2 ###
def is_palindrome(text):
    cleaned = text.replace(" ", "").lower()
    return cleaned == cleaned[::-1]
###correcton for exercise 2 done###
### cleaned[::-1] is the string reversed. A palindrome equals its own reverse, so no loop is needed.
### Your loop version is also correct. It just does by hand what [::-1] does in one step.
####### exercise 2 done #######


####### exercise 3 #######
### Write count_words(sentence), which returns a dictionary with how many times each word appears, ignoring capital letters.count_words("The cat and the hat") → {"the": 2, "cat": 1, "and": 1, "hat": 1}
### correction for exercise 3 ###
def count_words_corrected(sentence):
    counts = {}
    for word in sentence.lower().split():
        if word in counts:
            counts[word] += 1
        else:
            counts[word] = 1
    return counts
### correction for exercise 3 done ###
### .split() cuts a string at the spaces and returns a list of words: "the cat and the hat".split() → ["the", "cat", "and", "the", "hat"].
### counts = {} is an empty dictionary.
### if word in counts: seen before → add 1; otherwise → start at 1.
####### exercise 3 done #######

               