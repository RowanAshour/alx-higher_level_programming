#!/usr/bin/python3

# Print the ASCII alphabet in lowercase without a new line
print("".join("{:c}".format(char) for char in range(ord('a'), ord('z') + 1)), end='')
