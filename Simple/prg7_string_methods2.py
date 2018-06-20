#string methods continued

string = "i love python"

#index method
result = string.index('python')
print('index of python: {}'.format(result))

# index method throws a value error if the value is not present in the string.
#hence we use an alternative.

#find method

result = string.find("python")
print('find of python: {}'.format(result))

#find of an unknown value
result2 = string.find("Python")
print('find of absent value: {}'.format(result2))

#strip methd
x = "000I love python000"
result = x.strip("0")
print('strip of 0: {}'.format(result))

#left strip
result = x.lstrip("0")
print('lstrip of 0: {}'.format(result))

#right strip
result = x.rstrip("0")
print('rstrip of 0: {}'.format(result))

#empty strip to remove blank spaces
y = "python   "
result1 = len(y)
result2 = len(y.strip())
print("actual sting: " + y)
print("length of the actual string with spaces: {} ".format(result1))
print("length using empty strip: {}".format(result2))



