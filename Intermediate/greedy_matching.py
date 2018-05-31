# greedy matching: looks for a string that starts with "F" and ends with ":" but it will take the last possible ":"

import re # import regular expressions

str = "From: the string :" # string to be tested

greedy_match = re.findall('^F.*:', str) # ('^F.+:') - also works similar

print(greedy_match)
