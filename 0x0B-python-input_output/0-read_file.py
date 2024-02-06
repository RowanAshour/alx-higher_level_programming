#!/usr/bin/python3

<<<<<<< HEAD

def read_file(filename=""):
    with open(filename, "r", encoding="UTF-8") as f:
        print(f.read(), end="")
=======
def read_file(filename=""):
    with open(filename, encoding="utf-8") as file:
        # Read the content of the file and print it to stdout
        print(file.read(), end="")

>>>>>>> ed0d6b20f6870fa4fe0a4f00f343ce3eb7a6fa56
