"""The module contains an abstract Dataset class and a CSVDataset class.
It allows loading a CSV file into a pandas DataFrame, clening it from 
columns with only None values and saving the data into a new CSV file.
"""
from abc import ABC, abstractmethod
import datetime
import pandas as pd

class Dataset(ABC):
    """Abstract class to represent a dataset

    Abstract methods
    ----------------
    save_data()
    """
    @abstractmethod
    def _fetch_data(self):
        pass

    @abstractmethod
    def save_data(self):
        """Saves the transformed data to the target location."""

    @abstractmethod
    def _transform_data(self):
        pass

    @abstractmethod
    def _clean_data(self):
        pass

class CSVDataset(Dataset):
    """A class to represent a CSV dataset.

    While initializing the data from the source file is fetched into a pandas DataFrame.
    Then columns containing only None values are dropped and a new column 'timestamp'
    is added to store the current timestamp.

    
    Arguments
    ---------
    src_filepath : str
        A source file to be read
    target_filepath : str
        A target CSV file for the data to be saved in
    
    Methods
    -------
    save_data() -> None
        Saves the loaded, cleaned and transformed data to the target filepath
    """
    def __init__(self, src_filepath, target_filepath):
        self.src_filepath = src_filepath
        self.target_filepath = target_filepath
        self.data: pd.DataFrame = self._fetch_data()
        self._clean_data()
        self._transform_data()

    @property
    def src_filepath(self):
        """Source filepath of the dataset"""
        return self._src_filepath

    @src_filepath.setter
    def src_filepath(self, value):
        self._src_filepath = value

    @property
    def target_filepath(self):
        """Target filepath of the dataset"""
        return self._target_filepath

    @target_filepath.setter
    def target_filepath(self, value):
        self._target_filepath = value

    def _fetch_data(self):
        return pd.read_csv(self.src_filepath)

    def _transform_data(self):
        self.data['timestamp'] = datetime.datetime.now()

    def _clean_data(self):
        self.data.dropna(axis = "columns",inplace=True)

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return f"Data is fetched from '{self.src_filepath}':" + "\n" + str(self.data)

    def save_data(self):
        self.data.to_csv(self.target_filepath)

def main():
    """Test"""

    # Create a CSV dataset which includes cleaning
    # and transforming the data from the source
    test = CSVDataset('employment-data.csv', 'employment-data-cleaned.csv')

    # Save the data into the target CSV file
    test.save_data()

    print(test)

if __name__ == '__main__':
    main()
