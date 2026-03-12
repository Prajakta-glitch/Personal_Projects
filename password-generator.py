import random
import string
print("Password Generator")
length=int(input("Enter password length: "))
digits=input("Include numbers? (yes/no): ")
symbols=input("Include symbols? (yes/no): ")

a=string.ascii_letters

if digits=="yes":
    a+=string.digits
if symbols=="yes":
    a+=string.punctuation
    
password=''.join(random.choice(a) for i in range(length))
print("Your password: ", password)