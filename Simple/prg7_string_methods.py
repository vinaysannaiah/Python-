#string methods
string = "I love Python"
# counts the appearance of the given letter or word in the string.
print(string.count("a"))
print(string.count("love"))

#lowercase
print("lowercase: " + string.lower())

#uppercase
print("uppercase: " + string.upper())

#capitalize - capitalizes only the first letter of the string
print("Capitalize: " + string.capitalize())

#title - capitalizes the first letter of every word
print("title: " + string.title())

#checking
result = string.islower()
print("is lower: {}".format(result))

#similarly for isupper, istitle
result = string.isspace()
print("is space: {}".format(result))

# only alphabets?
result = string.isalpha()
print("only alphabets: {}".format(result)) # gives false due to the space in the given string
# similarly isdigit() is for only digits, isalnum() is for alphanumeric
