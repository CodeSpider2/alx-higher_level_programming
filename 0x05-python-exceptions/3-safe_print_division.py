#!/usr/bin/python3

def safe_print_division(a, b):
    """Print the divison of
    the values a and b 
    """
    try:
        value = a / b
    except (TypeError, ZeroDivisionError):
        value = None
    finally:
        print("Inside result{}".format(value))
    return (value)
