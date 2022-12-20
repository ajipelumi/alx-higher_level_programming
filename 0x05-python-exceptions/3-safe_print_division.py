#!/usr/bin/python3
def safe_print_division(a, b):
    """
    divides 2 integers and prints the result
    a: first integer
    b: second integer
    Return: the value of the division, otherwise: None
    """
    try:
        res = a / b  # divide integers
        return res
    except ZeroDivisionError:  # divisor is zero
        res = 0
        print("Inside result: None")
    finally:
        if res != 0:
            print("Inside result: {}".format(res))
