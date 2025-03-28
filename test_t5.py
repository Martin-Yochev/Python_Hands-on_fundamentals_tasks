"""Test cases for the t5_dice_simulation module."""

import t5_dice_simulation as t5
import pytest

def test_dice_roll():
    """Test if the roll method returns an integer between 1 and the number of sides."""
    dice = t5.Dice()
    for _ in range(100):
        assert dice.roll() in range(1, 7)
    dice = t5.Dice(10)
    for _ in range(100):
        assert dice.roll() in range(1, 11)

def test_dice_roll_value_error():
    """Test if the Dice class raises a ValueError when the input is not integer greater than 1."""
    with pytest.raises(ValueError, match="sides must be an integer greater than 1"):
        t5.Dice(0)
        t5.Dice(1)
        t5.Dice(-1)
        t5.Dice(1.5)
        t5.Dice("a")

def test_simulation_run_value_error():
    """Test if the Simulation class raises a ValueError
    when the inputs are not integer greater than 0."""
    with pytest.raises(ValueError, match="num_dices must be an integer greater than 0"):
        t5.Simulation(0, 100)
        t5.Simulation(-1, 100)
        t5.Simulation(1.5, 100)
        t5.Simulation("a", 100)
    with pytest.raises(ValueError, match="num_rolls must be an integer greater than 0"):
        t5.Simulation(2, 0)
        t5.Simulation(2, -1)
        t5.Simulation(2, 1.5)
        t5.Simulation(2, "a")
