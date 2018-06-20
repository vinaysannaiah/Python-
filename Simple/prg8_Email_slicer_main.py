#get user email addres
email = input("What is your Email address?: ").strip()

#slice out user name
user_name = email[:email.index("@")]

#slice domain name
domain_name = email[email.index("@") + 1 :]

#format message
message = "hey there your user name is {} and ur domain name is {}".format(user_name, domain_name)

#display out the message
print(message)
