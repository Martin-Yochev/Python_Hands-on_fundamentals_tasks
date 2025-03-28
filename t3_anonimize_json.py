"""The file 'data.json' is given with information about users and their friends.
This module loads the file, replace all names with None and save back the file
as json
"""
import json

def anonimize_name(x):
    """Anonimize an input list or dict where 'names' are converted to None.

    Args:
        x (dict | list): The input dictionary or list to be anonimized.
    """
    if isinstance(x, dict):
        if 'name' in x:
            x['name'] = None
        for key in x:
            anonimize_name(x[key])
    elif isinstance(x, list):
        for item in x:
            anonimize_name(item)

def main():
    """The main function of the module"""
    # Step 1: Open and load the file 'data.json'
    with open('data.json', mode='r', encoding='utf-8') as file:
        data = json.load(file)

    # Step 2: Anonimize the data
    anonimize_name(data)

    # Step 3: Save the data as another json file
    with open('anonimized_data.json', mode='w', encoding='utf-8') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()
