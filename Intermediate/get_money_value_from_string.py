# to get the money value from a string using the specific currensy character ex: "$" 

import re # import regular expressions

str = "the price of this items is $25.99 and the other one is $99.69" # string to be tested

get_money = re.findall('\$[0-9.]+', str) 

'''
\$ - look only for $ character
+ - extend further til the end of the string
. - to get floating point numbers
'''

print(get_money)

#output : ['$25.99', '$99.69']
