#!/usr/bin/python3

# Print numbers from 0 to 98 in decimal and hexadecimal
for num in range(99):
    print("{:d} = 0x{:x}".format(num, num), end='\n' if num == 98 else '\n')
