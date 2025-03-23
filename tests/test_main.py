import pytest
from main import multiply_numbers, sum_even_numbers


def test_sum_even_numbers():
    """Test sum_even_numbers function."""
    assert sum_even_numbers([1, 2, 3, 4, 5, 6]) == 12
    assert sum_even_numbers([0, -2, -4, -6]) == -12
    assert sum_even_numbers([1, 3, 5]) == 0
    assert sum_even_numbers([]) == 0


def test_multiply_numbers():
    """Test multiply_numbers function."""
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 5) == -5
    assert multiply_numbers(0, 10) == 0
    assert multiply_numbers(4, -2) == -8


if __name__ == "__main__":
    pytest.main()
