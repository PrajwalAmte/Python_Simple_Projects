import random
passlen = int(input("Enter the length of the Password: "))
s = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_"
p = "".join(random.sample(s, passlen))
print("Password: " + p)