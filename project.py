import random
import string

def make_password(length = 8):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ""
    for i in range(length):
        password = password + random.choice(characters)
    return password

n = int(input("Enter the length of the password: "))
print(make_password(n))