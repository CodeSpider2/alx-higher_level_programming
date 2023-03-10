#!/usr/bin/python3
# file: 0_add.py
# Amos Wachira as Author

if __name__ == "__main__":
    """Import a simple function and print sum."""
    from add_0 import add

    a = 1
    b = 2
    print("{} + {} = {}".format(a, b, add(a, b)))
