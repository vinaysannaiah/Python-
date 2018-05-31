# to get the hostname from a string using the "@" character

import re # import regular expressions

str = "From: the string get the email id: vinay.sannaiah@gmail.com to send an email" # string to be tested

get_host_name = re.findall('@([^ ]*)', str) 

'''
@ - character to be looked for
() - part of the string to be extracted once the character has been found
[^ ] - the extracted string must not start with a blank space
* - go till the end of that word i.e. until the next space 
'''

print(get_host_name)

#output : ['gmail.com']
