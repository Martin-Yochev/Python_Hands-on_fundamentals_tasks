"""The module contains classes CSVReader, JSONReader and DatabaseReader
which inherit from the abstract class Reader and implement the method read.
With the help of the class ReaderFactory the user can create a reader
object and read a CSV file, Json file or database table into a pandas
DataFrame object.
"""
from abc import ABC, abstractmethod
import sqlite3
import pandas as pd



class Reader(ABC):
    """Abstract class to represent a reader object.

    Attributes
    ----------
    filepath : str
        A file to be read

    Methods
    -------
    read()
        To be implemented
    """
    def __init__(self, filepath):
        self.filepath = filepath
        self.data = self.read()

    @property
    def filepath(self):
        """A file to be read"""
        return self._filepath

    @filepath.setter
    def filepath(self, value):
        self._filepath = value

    @abstractmethod
    def read(self):
        """read a file"""

class CSVReader(Reader):
    """Class to represent a file reader which reads from CSV file.

    Methods
    -------
    read() -> pd.DataFrame
        Read a CSV file into a pd.DataFrame
    """

    def read(self):
        return pd.read_csv(self.filepath)

    def __str__(self):
        return self.data.to_string(max_rows=20, max_cols=5, line_width=80,
                               max_colwidth = 25, show_dimensions=True)

    def __repr__(self):
        return self.data.to_string()

class JSONReader(Reader):
    """Class to represent a file reader which reads from JSON file.

    Methods
    -------
    read() -> pd.DataFrame
        Read a JSON file into a pd.DataFrame
    """

    def read(self):
        return pd.read_json(self.filepath)

    def __str__(self):
        return self.data.to_string(max_rows=20, max_cols=5, line_width=80,
                               max_colwidth = 25, show_dimensions=True)

    def __repr__(self):
        return self.data.to_string()

class DatabaseReader(Reader):
    """Class to represent a database reader.

    Attributes
    ----------
    table_name : str
        The name of the table from which the data is read
    connection : Connection
        Connection to the database
    data : pd.DataFrame
        The data in pandas DataFrame format

    Methods
    -------
    read() -> pd.DataFrame
        Reads all data from the self.table_name in a DataFrame format
    """
    def __init__(self, table_name: str, connection, filepath=None):
        self.table_name = table_name
        self.connection = connection
        super().__init__(filepath)

    @property
    def table_name(self):
        """the name of the table from which the data is read"""
        return self._table_name

    @table_name.setter
    def table_name(self, value):
        self._table_name = value

    @property
    def connection(self):
        """connection to the database"""
        return self._connection

    @connection.setter
    def connection(self, value):
        self._connection = value

    def read(self):
        return pd.read_sql(sql=f"SELECT * FROM {self.table_name}", con=self.connection)

    def __str__(self):
        return self.data.to_string(max_rows=20, show_dimensions=True)

    def __repr__(self):
        return self.data.to_string()

class ReaderFactory:
    """Class to generate a reader corresponsing to the needs.

    Methods
    -------
    get_reader(reader_type: str) : CSVReader | JSONReader | DatabaseReader
        Returns a reader based on the input
    """
    @staticmethod
    def get_reader(reader_type: str):
        """Returns a reader based on the input.
        """
        type : str = reader_type.lower()
        readers : dict[str, Any] = {
            'csv': CSVReader,
            'json': JSONReader,
            'database': DatabaseReader
        }
        try:
            return readers[type]
        except KeyError:
            raise ValueError("Reader type not supported")

def main():
    """Test the readers."""

    # Create a connection and cursor for the sqlite3 database and table 'users'
    conn = sqlite3.connect('users')

    # Insert the example data into the table

    cur = conn.cursor()
    cur.execute("""CREATE TABLE IF NOT EXISTS users(
       userid INT PRIMARY KEY,
       fname TEXT,
       company TEXT,
       gender TEXT,
       date DATE,
       amount FLOAT);
    """)
    users = [
        ('00001', 'Nik', 'datagy', 'male', '2023-06-01', 12.34),
        ('00002', 'Lois', 'Daily Planet', 'Female', '2023-07-01', 12.56),
        ('00003', 'Peter', 'Parker Tech', 'Male', '2023-08-01', 45.67),
        ('00004', 'Bruce', 'Wayne Enterprises', 'male', '2023-09-01', 123.12)
        ]
    # cur.executemany("INSERT INTO users VALUES(?, ?, ?, ?, ?, ?);", users)
    # conn.commit()

    # Create a 'database', 'csv' and 'json reader
    db_reader = ReaderFactory.get_reader('database')
    csv_reader = ReaderFactory.get_reader('csv')
    json_reader = ReaderFactory.get_reader('json')

    print("Results from the database reader:"+"\n")
    print(db_reader('users', conn))
    print("\n")

    print("Results from the csv reader:"+"\n")
    print(csv_reader('employment-data.csv'))
    print("\n")

    print("Results from the json reader:"+"\n")
    print(json_reader('data.json'))

if __name__ == "__main__":
    main()
