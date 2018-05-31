# To get the Email from a string using the "@" character

import re # import regular expressions

str = "From: the string get the email id: vinay.sannaiah@gmail.com to send an Email" # string to be tested

get_Email = re.findall('\S+@\S+', str) 

'''
\S - non blank character
+ - extend further to get the complete email id
@ - character to be looked for
'''

print(get_Email)

#output : ['vinay.sannaiah@gmail.com']
