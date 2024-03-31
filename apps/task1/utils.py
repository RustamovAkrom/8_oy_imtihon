import random
from string import digits, ascii_letters


def random_string(length: int = 30):
    return "".join([random.choice(digits + ascii_letters) for _ in range(length)])
