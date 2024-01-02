#!/usr/bin/python3

def fizzbuzz():
    """
    Print numbers from 1 to 100 following FizzBuzz rules.

    For multiples of three, print "Fizz"
    For multiples of five, print "Buzz"
    For multiples of both three and five, print "FizzBuzz"
    For other numbers, print the number itself

    Each element is followed by a space.

    Returns:
    - None
    """
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("FizzBuzz", end=' ')
        elif i % 3 == 0:
            print("Fizz", end=' ')
        elif i % 5 == 0:
            print("Buzz", end=' ')
        else:
            print(i, end=' ')


# Test the function
if __name__ == "__main__":
    fizzbuzz()
    print("")
