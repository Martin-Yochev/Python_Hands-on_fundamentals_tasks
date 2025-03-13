"""Python_Hands-on_tasks

This repository includes my solutions to the tasks in the course 'Python hands-on'.
Here are the tasks:

1. t1_generators.py
-------------------

  Create a set of functions that generate random words, dates and boolean values.
  Create a generator function that yields the row of random data.
  Create a function that uses the generator function and writes the data into a csv file.

2. t2_lambdas.py
----------------

  This is a series of small tasks using lambda functions.
  
  1. You have the following sentence as string:
      sentence = 'This is a lAmBdA FuNction task'
   - Split the sentence into a list
   - Write a lambda function that accepts the list of words returns multiple lists
     each list containing the actual word, the word uppercase, the word lowercase, the length of the word
     return the results as a 2d list
  
  2. You have the following sentence as string:
      sentence = 'This is a lAmBdA FuNction task'
   - Split the sentence into a list
   - write a series of functions that return a string uppercase, lowercase and the length of a string
   - create a list of those functions and use map to apply all functions to the sentence list
   return the results as a 2d list
  
  3. You have the following lists
   a = [1, 11, 23, 44, 16]
   b = [2, 3, 5, 6, 7, 8, 44, 16]
   Using a lambda function return a list with values that are common between the 2 lists
  
  4. You have the following sentence as string:
      sentence = 'This is a lAmBdA FuNction task'
   - Split the sentence into a list
   Using a lambda function sort the list by the last character of each word alphabetically

3. t3_anonimize_json.py + data.json
-----------------------------------

  You are given a file of users with information about them and their friends. There is an attribute 'name' which is considered sensitive. You are task is the  
  following:
  1. Load the json file in the appropriate python data structure
  2. Go through the json structure and replace all names with NULL / None values
  3. Save the file back as json
  Note: Have in mind you might encounter other cases where the json depth is different. The code needs to work with a json with any depth.

4. t4_decorators.py
-------------------

  You have the following string data = 'This is An exAmPlE StRinG' which is returned by the function get_data().
  Write the following decorators and apply all of them on the get_data() function:
  1. Split decorator that splits the string into words with a space separator
  2. Uppercase decorator that makes all words uppercase
  3. Filter decorator that removes all words with < 4 characters length
  What is the order of execution of the decorators? Is it from top to bottom or from bottom to the top?

5. t5_dice_simulation.py
------------------------

  Write a Dice and Simulation classes in order to simulate rolling of a dice.
  Display the results using matplotlib bar chart
  Which outcome happens more often than the other?
  What kind of distribution is this(you will need to perfrom big number of simulations for example 50000)?
  
  The Dice class should generate a number from 1 to 6 (1 dice roll)
  The simulation class should accept number of dices to be rolled:
  For example 2, which means the max sum will be 12
  The simulation class should accept number of rolls, for example 50000

6. t6_datasets.py + emplyment-data.csv
--------------------------------------

  Define the following classes:
  
  Dataset - abstract class with the following methods that need to be overriden
    _fetch_data()
    save_data()
    _transform_data()
    _clean_data()
  
  CSVDataset(src_filepath, target_filepath) – inherits Dataset and implements all its methods
    Define properties(getters, setters) for the src_filepath and target_filepath
    Implement __str__ magic method
    Implement __repr__ magic method
    _fetch_data() – reads data from the employment-data.csv file
    _clean_data() – drops na values
    _transform_data() – at this point in time, add a current timestamp column to the end of the dataframe
    save_data() – saves the transformed data to the target location as csv

7. t7_op_overloading.py
-----------------------

  Create a class called Distance with the following properties:
    meters
    centimetres
    millimetres
  Add all required getter, setter and__str__, __repr__ magic methods
  Implement functionality so that you can add and subtract distance objects. Think if you can implement add, subtract assignment operations as well(+=, -=).

8. t8_helper_and_utility_main.py + data-helper.py
-------------------------------------------------

  Create a utlity data-helper.py module which includes the following functions.
    get_random_date()
    get_random_string()
    get_random_integer()
    get_random_double()
  Create a separate main.py file where you can import the data-helper.py module and call all its functions. Print and format all results.
  Is there a problem importing a module with a dash('-') in its name? How can you do that?

9. t9_ reader_factory.py
------------------------

  Create the following class representation:
  
  Create an abstract Reader with methods:
    read()- abstract method
  Create a CSVReader inheriting from Reader and implementing read()
    read() – reads the contents of a csv file and returns it as pandas dataframe
  Create a JSONReader inheriting from Reader and implementing read()
    read() – reads the contents of a json file and returns it as pandas dataframe
  Create DatabaseReader – inheriting from Reader and implementing read()
    read() – reads a table from a db of your choice and returns it as pandas dataframe
  Create ReaderFactory class with methods:
    get_reader(reader_type: str) – static method that returns the reader based on the type that is passed
  Demonstrate how you can read data from the 3 sources through the ReaderFactory.get_reader(reader_type: str) method. Have in mind you are not limited to creating only the listed methods, feel free to modularize your code further and improve its design.

10. t10_pipelines_datasets_activities.py + users_1k.json
--------------------------------------------------------

  We will be developing a really simple class representation of Azure Data Factory ETL tool. 
  Pay attention to the way source, sink, dataset entities exist in Data Factory.
  Please use pandas for all data loading tasks. JSON file for testing
  Create the following classes:
  
  Dataset – abstract class with methods
    preview()
    show_schema()
    get_data()
    write_data()
  JSONDataset – inherits from Dataset and implements its methods
  CSVDataset – inherits from Dataset and implements its methods
  Source – has ‘Dataset’ as a property
  Sink – has ‘Dataset’ as a property
  Activity – abstract class with methods
    start()
  WaitActivity – inherits from Activity
  Implements start() – start accepts time_in_seconds and sleeps the program for the number of seconds
  CopyActivity – inherits from Activity
  Implements start() – start copies the data from the source to the sink
  Pipeline – has activities list of type Activity as a property and methods
    add_activity() – adds an activity to the pipeline
    execute() – iterates through the activities and executes them in order
"""
