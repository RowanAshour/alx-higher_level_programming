#!/usr/bin/python3

def pow(a, b):
    """
    Compute a to the power of b and return the value.

    Args:
    - a: base (integer)
    - b: exponent (integer)

    Returns:
    - The value of a ^ b
    """
    return a ** b


# Test the function
if __name__ == "__main__":
    print(pow(2, 2))
    print(pow(98, 2))
    print(pow(98, 0))
    print(pow(100, -2))
    print(pow(-4, 5))
