"""The file 'data.json' is given with information about users and their friends.
This module loads the file, replace all names with None and save back the file
as json
"""
import json

def main():
    # Step 1: Open and load the file 'data.json'
    with open('data.json', 'r') as file:
        data = json.load(file)

    def anonimize_name(x):
        """Anonimize an input where 'names' are converted to None

        The function takes the json file read above and replaces
        the value of each occurance of 'name' key with None. It
        checks also the depth of the file and replaces the 'names'
        on all levels.
        """
        if isinstance(x, dict):
            if 'name' in x:
                x['name'] = None
            for key in x:
                anonimize_name(x[key])
        elif isinstance(x, list):
            for item in x:
                anonimize_name(item)

    # Step 2: Anonimize the data
    anonimize_name(data)

    # Step 3: Save the data as another json file
    with open('anonimized_data.json', 'w') as file:
        json.dump(data, file, indent=4)

if __name__ == "__main__":
    main()
