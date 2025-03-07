"""Given is a sting returned from the function get_data.
The following decorators are used on the function in a
specific order:

fil
up
split_string

When three decorators are used on one function they are
executed from bottom to top. So, first the 'split_string'
is called to cerate a list from the string, than the 'up'
to make elements uppercase and finaly 'fil' to filter out
the short words.
"""

def main():
    """The main function of the module"""
    def split_string(func):
        """A decorator that splits the result string of the
        function being called into a list.
        """
        def wrapper():
            return func().split()
        return wrapper

    def up(func):
        """A decorator that takes every element from a result
        list and makes it uppercase.
        """
        def wrapper():
            return [i.upper() for i in func()]
        return wrapper

    def fil(func):
        """A decorator that filters all elements from a
        result list with length less than 4 out.
        """
        def wrapper():
            return [i for i in func() if len(i) > 3]
        return wrapper

    @fil
    @up
    @split_string

    def get_data():
        """Returns an example string"""
        return 'This is An exAmPlE StRinG'

    print(get_data())

if __name__ == "__main__":
    main()
