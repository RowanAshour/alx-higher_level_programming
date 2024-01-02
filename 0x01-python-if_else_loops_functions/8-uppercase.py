#!/usr/bin/python3

def uppercase(s):
    """
    Print a string in uppercase followed by a new line.

    Args:
    - s: a string

    Returns:
    - None
    """
    result = ""
    for char in s:
        # Check if the character is a lowercase letter
        if ord('a') <= ord(char) <= ord('z'):
            # Convert the lowercase letter to uppercase using ASCII adjustment
            result += "{:c}".format(ord(char) - ord('a') + ord('A'))
        else:
            # Append non-lowercase characters as they are
            result += char

    print(result)  # Print the modified string followed by a new line

# Test the function
if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")
