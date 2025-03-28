"""Test cases for the t3_anonimize_json module."""

import t3_anonimize_json

def test_anonimize_name():
    """Test if the anonimize_name function replaces all names with None."""
    data = {
        "name": "John",
        "age": 30,
        "friends": [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 35}
        ]
    }
    data2 = [
        {"name": "John", "age": 30, "friends": [
            {"name": "Alice", "age": 25},
            {"name": "Bob", "age": 35}
        ]},
        {"name": "Jane", "age": 40, "friends": [
            {"name": "Charlie", "age": 45},
            {"name": "David", "age": 55}
        ]},
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 35}
        ]
    t3_anonimize_json.anonimize_name(data) # input is dict
    assert data == {
        "name": None,
        "age": 30,
        "friends": [
            {"name": None, "age": 25},
            {"name": None, "age": 35}
        ]
    }
    t3_anonimize_json.anonimize_name(data2) # input is list
    assert data2 == [
        {"name": None, "age": 30, "friends": [
            {"name": None, "age": 25},
            {"name": None, "age": 35}
        ]},
        {"name": None, "age": 40, "friends": [
            {"name": None, "age": 45},
            {"name": None, "age": 55}
        ]},
        {"name": None, "age": 25},
        {"name": None, "age": 35}
        ]
