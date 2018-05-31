#This progrma gets all the upper case vowels with in a string

import re # import regular expressions

string = "Python Is A Very Friendly Programming Language"

upper_vowels = re.findall('[AEIOU]+', string) # look for the upper case vowels

print(upper_vowels) # print the result
