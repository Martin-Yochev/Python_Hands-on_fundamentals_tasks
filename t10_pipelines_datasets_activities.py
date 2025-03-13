"""This module contains JSONDataset and CSVDataset classes
which help developing pipelines from Source to Sink objects.
"""
import time
from abc import ABC, abstractmethod
import pandas as pd


class Dataset(ABC):
    """An abstract class to represent a dataset.

    Methods
    -------
    preview() -> pd.DataFrame
        Returns the first 5 rows
    show_schema() -> pd.Series
        Returns the dtypes in the dataset
    get_data() -> pd.DataFrame
        Returns the data of the dataset
    write_data(to_write_data) -> None
        Writes the given data into the dataset
    """

    @abstractmethod
    def preview(self):
        """Return the first 5 rows."""

    @abstractmethod
    def show_schema(self):
        """Return the dtypes in the dataset."""

    @abstractmethod
    def get_data(self):
        """Return the data of the dataset."""

    @abstractmethod
    def write_data(self, to_write_data: pd.DataFrame):
        """Write the given data into the dataset."""


class JSONDataset(Dataset):
    """A class to represent JSON datasets.

    Attributes
    ----------
    filepath : str
        Name of the filepath for the data
    data : pd.DataFrame
        The read data from the filepath or empty DataFrame if filepath not given
    """
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            self.data = pd.read_json(filepath, orient='records')
        except pd.errors.EmptyDataError:
            self.data = pd.DataFrame()

    def preview(self):
        return self.data.head()

    def show_schema(self):
        return self.data.dtypes

    def get_data(self):
        return self.data

    def write_data(self, to_write_data: pd.DataFrame):
        to_write_data.to_json(self.filepath)
        self.data = to_write_data

class CSVDataset(Dataset):
    """A class to represent CSV datasets.

    Attributes
    ----------
    filepath : str
        Name of the filepath for the data
    data : pd.DataFrame
        The read data from the filepath or empty DataFrame if filepath not given
    """
    def __init__(self, filepath):
        self.filepath = filepath
        try:
            self.data = pd.read_csv(filepath)
        except pd.errors.EmptyDataError:
            self.data = pd.DataFrame()

    def preview(self):
        return self.data.head()

    def show_schema(self):
        return self.data.dtypes

    def get_data(self):
        return self.data

    def write_data(self, to_write_data: pd.DataFrame):
        to_write_data.to_csv(self.filepath)
        self.data = to_write_data

class Source:
    """A class to represent a source object.

    Attributes
    ----------
    dataset : Dataset
        The dataset initiated with the source object

    Methods
    -------
    get_data() -> pd.DataFrame
        Returns the data of the dataset
    """
    def __init__(self, dataset: Dataset):
        self.dataset = dataset

    def get_data(self):
        """Returns the data of the dataset.
        """
        return self.dataset.get_data()

class Sink:
    """A class to represent a sink object.

    Attributes
    ----------
    dataset : Dataset
        The dataset initiated with the sink object

    Methods
    -------
    write_data(data) -> None
        Writes the given data into the dataset of the sink
    """
    def __init__(self, dataset: Dataset):
        self.dataset = dataset

    def write_data(self, data: pd.DataFrame):
        """Writes the given data into the dataset of the sink.
        """
        self.dataset.write_data(data)

class Activity(ABC):
    """An abstract class to represent an activity.

    Methods
    -------
    start() -> None
        Starts the activity
    """
    @abstractmethod
    def start(self):
        """Starts the activity"""

class WaitActivity(Activity):
    """A class to represent a wait activity.

    Attributes
    ----------
    seconds : int
        Number of seconds to wait

    Methods
    -------
    start() -> None
        Sleep for number of seconds
    """
    def __init__(self, seconds : int):
        self.seconds = seconds

    def start(self):
        time.sleep(self.seconds)

class CopyActivity(Activity):
    """A class to represent a copy activity. It copies 
    the data from the source to the sink.

    Attributes
    ----------
    source : Source
        A source object to copy from
    sink : Sink
        A sink object to copy to

    Methods
    -------
    start() -> None
        Gets the data from the source and writes it to the sink
    """
    def __init__(self, source: Source, sink: Sink):
        self.source = source
        self.sink = sink

    def start(self):
        data = self.source.get_data()
        self.sink.write_data(data)

class Pipeline():
    """A class to represent a pipeline of activities.

    Attributes
    ----------
    activities_list : list[Activity]
        The list of activities in the pipeline

    Methods
    -------
    add_activity(activity) -> None
        Appends the given activity to the list of the pipeline

    execute() -> None
        Starts every activity from the list one by one
    """
    def __init__(self):
        self.activities_list: list[Activity] = []

    def add_activity(self, activity : Activity):
        """Appends the given activity to the list of the pipeline.
        """
        self.activities_list.append(activity)

    def execute(self):
        """Starts every activity from the list one by one.
        """
        for activity in self.activities_list:
            activity.start()

def main():
    """Test with example JSON file."""

    # Create source and sink objects
    src = Source(JSONDataset('users_1k.json'))
    sink = Sink(CSVDataset('users_1kk.csv'))

    # Preview the empty sink dataset
    print(sink.dataset.preview())

    # Create a wait and copy activities
    wait = WaitActivity(5)
    copy_activity = CopyActivity(src, sink)

    # Add the activities to a pipeline
    pl = Pipeline()
    pl.add_activity(wait)
    pl.add_activity(copy_activity)

    # Execute the pipeline and preview the loaded sink dataset
    pl.execute()
    print(sink.dataset.preview())

if __name__ == "__main__":
    main()
