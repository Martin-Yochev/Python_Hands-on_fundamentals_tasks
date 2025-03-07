"""Generator of random words, dates and booleans.

Functions
---------
random_word -> str
    Returns a random word based on input length
random_date -> str
    Returns a random date between 1900 and 2025 as string
random_bool -> str
    Returns a random boolean as string
generate_random_data -> Generator[str, None, None]
    Takes a positive integer and yields that many rows of random data
write_into_csv -> None
    Writes random data in a file
"""

import random
import datetime
from typing import Generator

def random_word(n=8) -> str:
    """Takes a positive integer n and returns a random word with n characters.

    Parameters
    ----------
    n : int, optinal
        The length of the random word created (default is 8)

    Raises
    ------
    ValueError
        If the input is not integer or is not positive.
    """

    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    return ''.join(random.choices('abcdefghijklmnopqrstuvwxyz', k=n))

def random_date() -> str:
    """Returns a random date between years 1900 and 2025 as 
    string in format 'YYYY-MM-DD'.
    """

    year = random.randint(1900, 2025)
    month = random.randint(1, 12)

    # Check witch month and year are randomly choosen and
    # choose and random day
    if month in [4, 6, 9, 11]:
        day = random.randint(1, 30)
    elif month == 2:
        if year % 4 == 0:
            day = random.randint(1, 29)
        else:
            day = random.randint(1, 28)
    else:
        day = random.randint(1, 31)

    # Create a datetime object from the random variables and
    # remove the suffix seconds
    return str(datetime.datetime(year, month, day)).removesuffix(' 00:00:00')

def random_bool() -> str:
    """Returns a random boolean as string."""
    return str(random.choice([True, False]))

def generate_random_data(num_rows: int, word_length=8) -> Generator[str, None, None]:
    """Takes a positive integer num_rows and yields that many rows of random data.

    The format is '"num_of_row", "random_word", "random_date", "random_bool"'.
    Optionally also the length of the random word can be choosen with the
    parameter word_length.

    Parameters
    ----------
    num_rows : int
        The number of rows with random data to be yielded
    word_length : int, optional
        The number of characters in the random word

    Raises
    ------
    ValueError
        If the input is not integer or is not positive.
    """

    if not isinstance(num_rows, int) or num_rows <= 0:
        raise ValueError("n must be a positive integer")
    for i in range(1,num_rows+1):
        yield f'"{i}", "{random_word(word_length)}", "{random_date()}", "{random_bool()}"'

def write_into_csv(filename, num_rows: int, word_length=8) -> None:
    """Takes a file and writes n rows of random data in it.
    
    Parameters
    ----------
    filename : str
        The name or path of the file
    num_rows : int
        The number of random rows to be written in the file
    word_length : int, optional
        The length of the random words (default is 8)
    """
    with open(filename, 'w') as file:
        for line in generate_random_data(num_rows, word_length):
            file.write(line + '\n')

def main():
    # write_into_csv('random_data.csv', 20, 50)
    return

if __name__ == '__main__':
    main()
