import random
import string

def generate_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation 
    password = ''.join(random.choice(characters) for _ in range(length)) 
    return password

length = int(input("Input the desired length of your password: "))
password = generate_password(length) 
print(f"Generated password is: {password}")
