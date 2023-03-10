#!/usr/bin/python3
#0_add.py

if __name__ == "__main__":
    """import a simple function and print sum"""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
