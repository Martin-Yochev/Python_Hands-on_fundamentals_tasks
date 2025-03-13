"""The module contains the class Distance. The objects from the class
represent a linear distance in form 'm sm mm' and can be added and
substacted from each other.
"""
class Distance:
    """Represents a Distance object in form 'm cm mm'.
    ...

    Attributes
    ----------
    meters : int

    centimeters : int

    milimeters : int

    Raises
    ------
    ValueError
        If value is not a positive integer
    """
    def __init__(self, meters: int, centimeters: int, milimeters: int):
        self.meters = meters
        self.centimeters = centimeters
        self.milimeters = milimeters
        self._distribute()

    def _distribute(self):
        # a method called after initialization which distributes the metrics in
        # the correct way
        self.meters = self.meters + (self.centimeters + self.milimeters // 100) // 100
        self.centimeters = (self.centimeters + self.milimeters // 10) % 100
        self.milimeters = self.milimeters % 10

    @property
    def meters(self):
        """How much meters does the distance have."""
        return self._meters

    @meters.setter
    def meters(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("value must be non-negative integer")
        self._meters = value

    @property
    def centimeters(self):
        """How much centimeters does the distance have."""
        return self._centimeters

    @centimeters.setter
    def centimeters(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("value must be non-negative integer")
        self._centimeters = value

    @property
    def milimeters(self):
        """How much milimeters does the distance have."""
        return self._milimeters

    @milimeters.setter
    def milimeters(self, value):
        if not isinstance(value, int) or value < 0:
            raise ValueError("value must be non-negative integer")
        self._milimeters = value

    def __str__(self):
        return f"{self.meters}m {self.centimeters}cm {self.milimeters}mm"

    def __repr__(self):
        return f"{self.meters}m {self.centimeters}cm {self.milimeters}mm"

    def __add__(self, other: 'Distance'):
        result: Distance = Distance(0,0,0)
        result.meters = self.meters + other.meters
        result.centimeters = self.centimeters + other.centimeters
        result.milimeters = self.milimeters + other.milimeters
        result._distribute()
        return result

    def __iadd__(self, other):
        self.meters = self.meters + other.meters
        self.centimeters = self.centimeters + other.centimeters
        self.milimeters = self.milimeters + other.milimeters
        self._distribute()
        return self

    def __sub__(self, other):
        result: Distance = Distance(0,0,0)
        result.meters = self.meters - other.meters
        result.centimeters = self.centimeters - other.centimeters
        result.milimeters = self.milimeters - other.milimeters
        result._distribute()
        return result

    def __isub__(self, other):
        self.meters = self.meters - other.meters
        self.centimeters = self.centimeters - other.centimeters
        self.milimeters = self.milimeters - other.milimeters
        self._distribute()
        return self

def main():
    """Test with some examples"""
    d1 = Distance(1, 150, 150)
    d2 = Distance(0, 50, 50)

    print(f"Distance object d1: {d1}")
    print(f"Distance object d2: {d2}")
    print(f"Result for d1 - d2: {d1 - d2}")
    d1 += d2
    print(f"Object d1 after adding and assigning d2 to d1: {d1}")
if __name__ == '__main__':
    main()
