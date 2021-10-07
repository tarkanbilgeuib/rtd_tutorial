""" Module to test out Sphinx automatic documentation """

def my_func(word):
    """ An overdocumented print function

    Parameters
    ----------
    word : str
        A word to print.
    """
    print(word)

def my_rst_function(number):
    """
    Multiplies a number by two.

    :param number: this is a number
    :returns: the number multiplied by two
    """
    return_value = number * 2
    return return_value
