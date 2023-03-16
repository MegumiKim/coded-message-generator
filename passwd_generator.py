import string
import secrets
import random

# homemade strong password generator
def passwd_generator():
    password = secrets.token_urlsafe(10) + random.choice(string.punctuation)
    return password

print(passwd_generator())

