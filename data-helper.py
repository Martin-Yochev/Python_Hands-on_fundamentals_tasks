"""The module contains helper functions to generate random values:

get_random_date() -> str
    random date between years 1900 and 2025 as string
get_random_string() -> str
    random string of 1 to 10 lowercase characters
get_random_integer() -> int
    random integer between 1 and 1000
get_random_double() -> float
    random float between 1 and 1000
"""
import random
import datetime

def get_random_date():
    """Generating random date between years 1900 and 2025 as string."""
    year = random.randint(1900, 2025)
    month = random.randint(1, 12)
    if month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    elif month == 2:
        if year % 4 == 0:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    else:
        day = random.randint(1, 31)

    return str(datetime.datetime(year, month, day))

def get_random_string():
    """Generates a random string of 1 to 10 lowercase characters."""
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k = random.randint(1, 10)))

def get_random_integer():
    """Generates a random integer between 1 and 1000."""
    return random.randint(1, 1000)

def get_random_double():
    """Generates a random float between 1 and 1000."""
    return random.uniform(1, 1000)
