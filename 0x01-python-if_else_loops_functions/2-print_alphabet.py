#!/usr/bin/python3

# Print the ASCII alphabet in lowercase without a new line
for char in range(ord('a'), ord('z') + 1):
    print("{:c}".format(char), end='')

# Print a new line at the end
print()
