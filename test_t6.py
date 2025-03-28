"""Test cases for the t6_datasets module."""

import t6_datasets as t6
import pandas as pd

def test_CSVDataset_with_mocker(mocker):
    """Test if the CSVDataset class reads the CSV file correctly
    and returns the correct data."
    """
    # Mock the read_csv function and return a DataFrame with an empty column
    mocker.patch("pandas.read_csv", return_value=pd.DataFrame({"a": [1, 2, 3],
                                                               "b": [4, 5, 6],
                                                               "c": [None, None, None]}))

    # Mock the _transform_data method
    mocker_transform_data = mocker.patch("t6_datasets.CSVDataset._transform_data")

    # Mock the to_csv method
    mocker_to_csv = mocker.patch("pandas.DataFrame.to_csv")

    # Create a CSVDataset object and save the data
    dataset = t6.CSVDataset("test_source.csv", "test_target.csv")
    dataset.save_data()

    # Assertions
    assert dataset.data.equals(pd.DataFrame({"a": [1, 2, 3], "b": [4, 5, 6]}))
    mocker_transform_data.assert_called_once()
    mocker_to_csv.assert_called_once_with("test_target.csv")
