"""The module contains a Dice and Simulation classes in
order to simulate rolling a dice and display the results
using matplotlib bar chart.
"""
import random
import matplotlib.pyplot as plt

class Dice:
    """A class used to represent a Dice
    ...

    Attributes
    ----------
    sides : int, optional
        the number of sides the dice has (default 6)
    

    Methods
    -------
    roll() -> int
        returns a random integer from one of the sides
    """

    def __init__(self, sides=6):
        if not isinstance(sides, int) or sides <= 1:
            raise ValueError("sides must be an integer greater than 1")
        self.sides = sides

    def roll(self) -> int:
        """Returns a random integer from one of the sides"""
        return random.randint(1, self.sides)

class Simulation:
    """A class to represent a simulation of rolling a dice
    ...

    Attributes
    ----------
    num_dices : int
        the number of dices to be rolled in the simulation
    num_rolls : int
        the number of rolls to be simulated
    dice_sides : int, optional
        number of sides of the dices
    dices : list[Dice]
        a list with Dice objects for the simulation
    results : dict[int,int]
        a result dict where keys are the possible summed result
        and the values are the occurances of the results in the
        simulation (initially values are 0)

    Methods
    -------
    run() -> None
        runs the simulation and populates the results with the
        corresponding occurances
    __str__() -> str
        creates and shows a bar chart displaying the results and
        prints the results of the simulation
    """
    def __init__(self, num_dices: int, num_rolls: int, dice_sides=6):
        if not isinstance(num_dices, int) or num_dices <= 0:
            raise ValueError("num_dices must be an integer greater than 0")
        if not isinstance(num_rolls, int) or num_rolls <= 0:
            raise ValueError("num_rolls must be an integer greater than 0")
        self.num_dices = num_dices
        self.num_rolls = num_rolls
        self.dice_sides = dice_sides
        self.dices: list[Dice] = [Dice(dice_sides) for _ in range(num_dices)]
        self.results: dict[int,int] = {i: 0 for i in range(num_dices,num_dices * dice_sides +1)}

    def run(self) -> None:
        """For every roll from num_rolls the function summs the
        dices rolled and adds 1 to the corresponding result in the
        results dict
        """
        for _ in range(self.num_rolls):
            temp = sum(dice.roll() for dice in self.dices)
            self.results[temp] += 1

    def __str__(self):
        plt.bar(self.results.keys(), self.results.values())
        plt.title("Dice outcomes")
        plt.xlabel("Sum of rolls")
        plt.ylabel("Num of rolls per outcome")
        plt.show()
        return '\n'.join(f'{k} -> {v} times' for k,v in self.results.items())

def main():
    """The main function of the module"""
    # Create a simulation with 2 dices and 50000 rolls
    sim = Simulation(num_dices=2, num_rolls=50000,dice_sides=6)

    # Run the simulation
    sim.run()

    # Print the results
    print(sim)

if __name__ == '__main__':
    main()
