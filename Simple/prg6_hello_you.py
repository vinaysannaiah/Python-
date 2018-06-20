#user input
#comments
#Ask user for name
name = input('What is your name?: \n')

#Ask user for the age
age = int(input("What is your age?: \n"))

#ask user for city
city = input("In which city do you live?: \n")

#Ask user what they enjoy
hobbies = input("What are your hobbies?: \n")

#create output text
output = "Hello " + name + " your age is " + str(age) + " you live in " + city +" city " + " and your hobbies are " + hobbies + "."

# anther way
string = "hello {} your age is {}. You live in {} city and your hobbies are {}"
output2 = string.format(name,age,city,hobbies)
print(output2)


#print output string
print(output)

#string Formatting
print("{} {}".format(name,age))

# or another way to change the order
print("{} {}".format(age,name))
print("{1} {0}".format(age,name)) # here as age is given first in order to make it appear in the 2nd position we enter the number position.
#numbering in python starts from 0 so in the above function name gets printed first and then goes the age.

