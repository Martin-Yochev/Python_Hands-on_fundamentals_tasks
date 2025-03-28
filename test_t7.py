"""Test cases for the t7_op_overloading module."""
import t7_op_overloading as t7
import pytest

@pytest.fixture
def distance():
    return t7.Distance(2, 80, 233)

def test_distance_value_error():
    """Test if the Distance class raises a ValueError
    when the inputs are not integers or are negative."""
    with pytest.raises(ValueError,
                       match="meters, centimeters and milimeters must be non-negative integers"):
        t7.Distance(-1, 80, 233)
        t7.Distance(2, -80, 233)
        t7.Distance(2, 80, -233)
        t7.Distance(2.5, 80, 233)
        t7.Distance(2, 80.5, 233)
        t7.Distance(2, 80, 233.5)
        t7.Distance("a", 80, 233)
        t7.Distance(2, "a", 233)
        t7.Distance(2, 80, "a")

def test_distance_distribution(distance):
    """Test if the distance is distributed correctly."""
    assert distance.meters == 3
    assert distance.centimeters == 3
    assert distance.milimeters == 3
    assert distance.total_milimeters == 3033

def test_distance_addition(distance):
    """Test if the addition operator works correctly."""
    distance2 = t7.Distance(1, 21, 20)
    result = distance + distance2
    assert result.meters == 4
    assert result.centimeters == 26
    assert result.milimeters == 3

def test_distance_iaddition(distance):
    """Test if the in-place addition operator works correctly."""
    distance2 = t7.Distance(1, 21, 20)
    distance += distance2
    assert distance.meters == 4
    assert distance.centimeters == 26
    assert distance.milimeters == 3

def test_distance_subtraction(distance):
    """Test if the subtraction operator works correctly."""
    distance2 = t7.Distance(1, 21, 20)
    result = distance - distance2
    assert result.meters == 1
    assert result.centimeters == 80
    assert result.milimeters == 3

def test_distance_isubtraction(distance):
    """Test if the in-place subtraction operator works correctly."""
    distance2 = t7.Distance(1, 21, 20)
    distance -= distance2
    assert distance.meters == 1
    assert distance.centimeters == 80
    assert distance.milimeters == 3

def test_distance_subtraction_negative(distance):
    """Test if the subtraction operator raises a ValueError when the result is negative."""
    distance2 = t7.Distance(3, 21, 20)
    with pytest.raises(ValueError, match="Resulting distance cannot be negative"):
        res = distance - distance2
