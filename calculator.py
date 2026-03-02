import math
# Maximum allowed value for factorial
MAX_FACTORIAL_LIMIT = 10

def square_root(x: float) -> float:
    """
    Returns the square root of a number.
    Raises ValueError if number is negative.
    """
    if x < 0:
        raise ValueError("Square root not defined for negative numbers")
    return math.sqrt(x)


def factorial(n):
    if not isinstance(n, int):
        raise ValueError("Factorial is only defined for integers.")

    if n < 0:
        raise ValueError("Factorial is not defined for negative numbers.")

    if n > MAX_FACTORIAL_LIMIT:
        raise ValueError(
            f"Factorial for numbers greater than {MAX_FACTORIAL_LIMIT} is restricted to prevent heavy computation."
        )

    return math.factorial(n)


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