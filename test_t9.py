"""Test cases for the t9_reader_factory module."""
import sqlite3
import os
import tempfile
import pytest
import pandas as pd
import t9_reader_factory as t9

def test_csv_reader():
    """Test if the CSVReader class reads a
    CSV file correctly."""
    # Create a temporary CSV file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    temp_file.write(b"col1,col2,col3\n1,2,3\n4,5,6")
    temp_file.close()

    # Create a CSVReader object
    reader = t9.CSVReader(temp_file.name)

    # Read the data from the CSV file
    data = reader.data

    # Check if the data is read correctly
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (2, 3)
    assert list(data.columns) == ['col1', 'col2', 'col3']
    assert data.iloc[0].tolist() == [1, 2, 3]
    assert data.iloc[1].tolist() == [4, 5, 6]

    # Clean up the temporary file
    os.remove(temp_file.name)

def test_json_reader():
    """Test if the JSONReader class reads a
    JSON file correctly."""
    # Create a temporary JSON file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
    temp_file.write(b'{"col1": [1, 4], "col2": [2, 5], "col3": [3, 6]}')
    temp_file.close()

    # Create a JSONReader object
    reader = t9.JSONReader(temp_file.name)

    # Read the data from the JSON file
    data = reader.data

    # Check if the data is read correctly
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (2, 3)
    assert list(data.columns) == ['col1', 'col2', 'col3']
    assert data.iloc[0].tolist() == [1, 2, 3]
    assert data.iloc[1].tolist() == [4, 5, 6]

    # Clean up the temporary file
    os.remove(temp_file.name)

def test_database_reader():
    """Test if the DatabaseReader class reads a
    database table correctly."""
    # Create a temporary SQLite database
    temp_db = tempfile.NamedTemporaryFile(delete=False, suffix='.db')
    conn = sqlite3.connect(temp_db.name)
    cursor = conn.cursor()

    # Create a sample table and insert data
    cursor.execute("CREATE TABLE test_table (col1 INTEGER, col2 INTEGER, col3 INTEGER)")
    cursor.execute("INSERT INTO test_table (col1, col2, col3) VALUES (1, 2, 3), (4, 5, 6)")
    conn.commit()

    # Create a DatabaseReader object
    reader = t9.DatabaseReader("test_table", conn)

    # Read the data from the database table
    data = reader.data

    # Check if the data is read correctly
    assert isinstance(data, pd.DataFrame)
    assert data.shape == (2, 3)
    assert list(data.columns) == ['col1', 'col2', 'col3']
    assert data.iloc[0].tolist() == [1, 2, 3]
    assert data.iloc[1].tolist() == [4, 5, 6]

    # Clean up the temporary database
    conn.close()
    temp_db.close()
    os.remove(temp_db.name)

def test_reader_factory_value_error():
    """Test if the ReaderFactory raises a ValueError
    when the reader type is not supported."""
    with pytest.raises(ValueError, match="Reader type not supported"):
        t9.ReaderFactory.get_reader('unsupported_type')
