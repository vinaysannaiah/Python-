import re

string = "Python Is A Very Friendly Programming Language"

upper_vowels = re.findall('[AEIOU]+', string)

print(upper_vowels)
