#!/usr/bin/python3

def uppercase(s):
    """
    Print a string in uppercase followed by a new line.

    Args:
    - s: a string

    Returns:
    - None
    """
    for char in s:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase letter to uppercase using ASCII adjustment
            print("{:c}".format(ord(char) - ord('a') + ord('A')), end='')
        else:
            # Print non-lowercase characters as they are
            print(char, end='')
    print()  # Add a new line at the end


# Test the function
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
