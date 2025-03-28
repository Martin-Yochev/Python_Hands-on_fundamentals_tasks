"""Test cases for the t1_generators module."""

import os
import t1_generators as t1
import pytest

def test_random_word_length():
    """Test if the random_word function returns a string with the correct length."""
    assert len(t1.random_word()) == 8
    assert len(t1.random_word(10)) == 10
    assert len(t1.random_word(1)) == 1

def test_random_word_characters():
    """Test if the random_word function returns a string with only alphabetical characters."""
    assert t1.random_word().isalpha()
    assert t1.random_word(10).isalpha()
    assert t1.random_word(1).isalpha()

def test_random_word_value_error():
    """Test if the random_word function raises a ValueError
    when the input is not an integer or is not positive."""
    with pytest.raises(ValueError, match="n must be a positive integer"):
        t1.random_word(-1)
        t1.random_word(0)
        t1.random_word(1.5)
        t1.random_word("a")

def test_random_date():
    """Test if the random_date function returns a string with the correct format."""
    assert t1.random_date().count("-") == 2
    assert len(t1.random_date()) == 10

def test_random_bool():
    """Test if the random_bool function returns a string with 'True' or 'False'."""
    assert t1.random_bool() in ["True", "False"]

def test_generate_random_data():
    """Test if the generate_random_data function returns
    a Generator object with the correct number of rows."""
    gen = t1.generate_random_data(3)
    assert isinstance(gen, t1.Generator)
    assert len(list(gen)) == 3

def test_generate_random_data_value_error():
    """Test if the generate_random_data function raises a ValueError
    when the input is not an integer or is not positive."""
    with pytest.raises(ValueError, match="num_rows must be a positive integer"):
        t1.generate_random_data(-1)
        t1.generate_random_data(0)
        t1.generate_random_data(1.5)
        t1.generate_random_data("a")

def test_write_into_csv():
    """Test if the write_into_csv function creates a file with the correct number of rows."""
    t1.write_into_csv('test.csv', 3)
    with open('test.csv', mode='r', encoding='utf-8') as file:
        assert len(list(file)) == 3
    os.remove('test.csv')
