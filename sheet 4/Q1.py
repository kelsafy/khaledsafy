import random

def generate_Password(length, chars):
    Password = ''.join(random.choices(chars, k=length))
    return Password

print(generate_Password(8, "abcde"))

