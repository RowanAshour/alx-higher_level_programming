#!/usr/bin/python3

def islower(c):
    """
    Check if a character is lowercase.

    Args:
    - c: a character (string of length 1)

    Returns:
    - True if c is lowercase
    - False otherwise
    """
    return ord(c) >= ord('a') and ord(c) <= ord('z')


# Test the function
if __name__ == "__main__":
    print("a is {}".format("lower" if islower("a") else "upper"))
    print("H is {}".format("lower" if islower("H") else "upper"))
    print("A is {}".format("lower" if islower("A") else "upper"))
    print("3 is {}".format("lower" if islower("3") else "upper"))
    print("g is {}".format("lower" if islower("g") else "upper"))
