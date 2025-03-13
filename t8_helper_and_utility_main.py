"""Here the 'data-helper.py' module is imported and
its functions are called.
"""
import importlib
# Because of the dash in the name of the module 'data-helper',
# it is imported using the importlib.import_module function
data_helper =importlib.import_module('data-helper')

def main():
    """Printing a random data, string, integer and double
    from the 'data-helper' module.
    """
    print('\n'.join(["Random date: " + data_helper.get_random_date()[:-9],
                    "Random string: " + data_helper.get_random_string(),
                    "Random integer: " + str(data_helper.get_random_integer()),
                    "Random double: " + f"{data_helper.get_random_double():.3f}"]))

if __name__ == "__main__":
    main()
