def safe_print_integer_err(value):
    """
    prints an integer
    value: can be any type (integer, string, etc.)
    Return: True if value has been correctly printed, otherwise False
    """
    try:
        print("{:d}".format(value))  # print integer
    except Exception as e:  # value is not of type int
        print("Exception: {}".format(e))  # print exception
        return False
    return True
