# Email Slicer
# _____________

email = input("Enter email : ")

username = email[:email.index("@")]
domain_name = email[email.index("@") + 1:]

print("Username    : ",username)
print("Domain name : ",domain_name)

# sample output
# ---------------------------------------------
# Enter email : aniketsingh7855@gmail.com
# Username    :  aniketsingh7855
# Domain name :  gmail.com
# ---------------------------------------------