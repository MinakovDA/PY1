import string
from random import sample

def random_letters(a=8) -> str:
    if a <= 0:
        raise ValueError("Длина пароля должна быть больше нуля")
    all_ = string.ascii_lowercase + string.digits + string.ascii_uppercase
    password = ''.join(sample(all_, a))
    return password

print(random_letters())