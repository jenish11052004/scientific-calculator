import math


def square_root(x: float) -> float:
    """
    Returns the square root of a number.
    Raises ValueError if number is negative.
    """
    if x < 0:
        raise ValueError("Square root not defined for negative numbers")
    return math.sqrt(x)


def factorial(x: int) -> int:
    """
    Returns factorial of a non-negative integer.
    Raises ValueError for negative or non-integer values.
    """
    if x < 0:
        raise ValueError("Factorial not defined for negative numbers")
    if not isinstance(x, int):
        raise ValueError("Factorial only defined for integers")
    return math.factorial(x)


def natural_log(x: float) -> float:
    """
    Returns natural logarithm (base e).
    Raises ValueError if x <= 0.
    """
    if x <= 0:
        raise ValueError("Natural logarithm only defined for positive numbers")
    return math.log(x)


def power(x: float, b: float) -> float:
    """
    Returns x raised to power b.
    """
    return math.pow(x, b)