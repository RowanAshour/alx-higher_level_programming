#!/usr/bin/python3

# Print the ASCII alphabet in lowercase excluding 'q' and 'e' without a new line
print("".join("{:c}".format(char) for char in range(ord('a'), ord('z') + 1) 
               if chr(char) not in ['e', 'q']), end='')
