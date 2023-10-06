from random import sample

length = int(input("Enter the length of password  :"))
password_set = "abcdefghijklmnopqrstuvwxyz1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()"
password = "".join(sample(password_set,length))
print("Generated password : ",password)

# sample output
# -----------------------------------
# Enter the length of password  :8
# Generated password :  Q4!0HCOS
# -----------------------------------