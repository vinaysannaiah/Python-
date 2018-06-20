#Email slicier or string slicer

word = "supercalifragilisticexpialidocious"
print(word[2])
#variable[start:end:step]
print(word[0:20:1])
print(word[0:5])#by defualt step is 1
print("step 2 for super: " + word[0:5:2])

#micro challenge to pick up cali
print(word[5:9:1])

#blanks
print(word[5::1])# when end is left blank it takes the value of the last index of the string

#reverse the string
print(word[::-1])

#reverse counting
print(word[-2])# checks from the revrse order of the string and prints the second bit here it is u.

#automated with index function
#to pick up cali
result = word[word.index("cali"):word.index("frag")]
print("pick up cali: " + result)

#pick up docious
print(word[word.index("docious"):])

#pick up fagilistic
print(word[word.index("fragilistic"):word.index("exp")])
