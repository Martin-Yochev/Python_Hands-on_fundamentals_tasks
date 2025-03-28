"""Test cases for the t4_decorators module."""

import t4_decorators

def test_split_string():
    """Test if the split_string decorator returns a list with the words of the input."""
    @t4_decorators.split_string
    def get_data():
        return 'This is An exAmPlE StRinG'
    assert get_data() == ['This', 'is', 'An', 'exAmPlE', 'StRinG']

def test_up():
    """Test if the up decorator returns a list with the words in uppercase."""
    @t4_decorators.up
    def get_data():
        return ['This', 'is', 'An', 'exAmPlE', 'StRinG']
    assert get_data() == ['THIS', 'IS', 'AN', 'EXAMPLE', 'STRING']

def test_fil():
    """Test if the fil decorator returns a list with the words longer than 3 characters."""
    @t4_decorators.fil
    def get_data():
        return ['THIS', 'IS', 'AN', 'EXAMPLE', 'STRING']
    assert get_data() == ['THIS', 'EXAMPLE', 'STRING']
