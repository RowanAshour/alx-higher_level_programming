#!/usr/bin/python3

def print_last_digit(number):
    """
    Print the last digit of a number and return its value.

    Args:
    - number: an integer

    Returns:
    - The value of the last digit
    """
    last_digit = abs(number) % 10
    print(last_digit, end='')
    return last_digit


# Test the function
if __name__ == "__main__":
    print_last_digit(98)
    print_last_digit(0)
    r = print_last_digit(-1024)
    print(r)
