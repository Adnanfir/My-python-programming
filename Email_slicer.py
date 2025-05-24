email=input("Enter your Email")
user=email[:email.index('@')]
domain=email[email.index('@')+1:]
output="Your username is {} and your domain is {}".format(user,domain)
print(email)
print("Hell0 ",user)
print(output)