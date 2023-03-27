#!/usr/bin/python3

def safe_print_division(a, b):
    """Print the divison of
    the values a and b 
    """
    value = 0
    try:
        value = a / b
    except:
        continue
    finally:
        print("{}".format(value), end="")
    return (value)
