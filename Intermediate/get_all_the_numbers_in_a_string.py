# this program can fetch all the numbers with in a string and create a list of all those numbers

import re # import regular expressions

str = "get 1 all 2 the 3 numbers 4 in 5 a 6 string 7 as 8 a 9 list 10" # string to be tested

nums = list() # empty list

nums = re.findall('[0-9]+', str) # look for the numbers in the string

print(nums) # print the numbers
