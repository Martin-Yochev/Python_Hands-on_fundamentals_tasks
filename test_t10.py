"""Test cases for the t10_pipelines_datasets_activities module."""
import tempfile
import os
import pandas as pd
import t10_pipelines_datasets_activities as t10


def test_json_dataset():
    """Test if the JSONDataset and Source class reads a JSON file correctly."""
    # Create a temporary JSON file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
    temp_file.write(b'{"col1": [1, 4], "col2": [2, 5], "col3": [3, 6]}')
    temp_file.close()

    json_dataset = t10.JSONDataset(temp_file.name)
    source = t10.Source(json_dataset)
    data = source.get_data()

    assert isinstance(data, pd.DataFrame)
    assert data.shape == (2, 3)
    assert list(data.columns) == ['col1', 'col2', 'col3']
    assert data.iloc[0].tolist() == [1, 2, 3]
    assert data.iloc[1].tolist() == [4, 5, 6]

    os.remove(temp_file.name)

def test_csv_dataset():
    """Test if the CSVDataset and Source class reads a CSV file correctly."""
    # Create a temporary CSV file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    temp_file.write(b"col1,col2,col3\n1,2,3\n4,5,6")
    temp_file.close()

    csv_dataset = t10.CSVDataset(temp_file.name)
    source = t10.Source(csv_dataset)
    data = source.get_data()

    assert isinstance(data, pd.DataFrame)
    assert data.shape == (2, 3)
    assert list(data.columns) == ['col1', 'col2', 'col3']
    assert data.iloc[0].tolist() == [1, 2, 3]
    assert data.iloc[1].tolist() == [4, 5, 6]

    os.remove(temp_file.name)

def test_sink():
    """Test if the Sink class writes data to a CSV file correctly."""
    # Create a temporary CSV file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    temp_file.close()

    csv_dataset = t10.CSVDataset(temp_file.name)
    sink = t10.Sink(csv_dataset)

    # Create a DataFrame to write to the sink
    data = pd.DataFrame({'col1': [1, 4], 'col2': [2, 5], 'col3': [3, 6]})
    sink.write_data(data)

    # Read the data back from the CSV file
    written_data = sink.dataset.get_data()

    assert isinstance(written_data, pd.DataFrame)
    assert written_data.shape == (2, 3)
    assert list(written_data.columns) == ['col1', 'col2', 'col3']
    assert written_data.iloc[0].tolist() == [1, 2, 3]
    assert written_data.iloc[1].tolist() == [4, 5, 6]

    os.remove(temp_file.name)

def test_wait_activity():
    """Test if the WaitActivity class waits for the specified time."""
    # Create a WaitActivity object with a 1-second wait time
    wait_activity = t10.WaitActivity(1)

    # Start the activity and check if it completes without errors
    wait_activity.start()

def test_copy_activity():
    """Test if the CopyActivity class copies data correctly."""
    # Create a temporary source and sink
    temp_source_file = tempfile.NamedTemporaryFile(delete=False, suffix='.json')
    temp_source_file.write(b'{"col1": [1, 4], "col2": [2, 5], "col3": [3, 6]}')
    temp_source_file.close()

    temp_sink_file = tempfile.NamedTemporaryFile(delete=False, suffix='.csv')
    temp_sink_file.close()

    # Create source and sink objects
    src = t10.Source(t10.JSONDataset(temp_source_file.name))
    sink = t10.Sink(t10.CSVDataset(temp_sink_file.name))

    # Create a copy activity
    copy_activity = t10.CopyActivity(src, sink)

    # Start the activity and check if it completes without errors
    copy_activity.start()

    # Read the data back from the sink
    written_data = sink.dataset.get_data()

    assert isinstance(written_data, pd.DataFrame)
    assert written_data.shape == (2, 3)
    assert list(written_data.columns) == ['col1', 'col2', 'col3']
    assert written_data.iloc[0].tolist() == [1, 2, 3]
    assert written_data.iloc[1].tolist() == [4, 5, 6]

    os.remove(temp_source_file.name)
    os.remove(temp_sink_file.name)
