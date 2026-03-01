import pytest
from calculator import square_root, factorial, natural_log, power


# -----------------------
# Square Root Tests
# -----------------------

def test_square_root_positive():
    assert square_root(16) == 4.0


def test_square_root_zero():
    assert square_root(0) == 0.0


def test_square_root_negative():
    with pytest.raises(ValueError):
        square_root(-4)


# -----------------------
# Factorial Tests
# -----------------------

def test_factorial_positive():
    assert factorial(5) == 120


def test_factorial_zero():
    assert factorial(0) == 1


def test_factorial_negative():
    with pytest.raises(ValueError):
        factorial(-5)


def test_factorial_float():
    with pytest.raises(ValueError):
        factorial(3.5)


# -----------------------
# Natural Log Tests
# -----------------------

def test_natural_log_valid():
    assert natural_log(1) == 0.0


def test_natural_log_positive():
    assert natural_log(10) > 0


def test_natural_log_zero():
    with pytest.raises(ValueError):
        natural_log(0)


def test_natural_log_negative():
    with pytest.raises(ValueError):
        natural_log(-2)


# -----------------------
# Power Function Tests
# -----------------------

def test_power_integers():
    assert power(2, 3) == 8.0


def test_power_float_base():
    assert power(2.5, 2) == 6.25


def test_power_zero_exponent():
    assert power(5, 0) == 1.0