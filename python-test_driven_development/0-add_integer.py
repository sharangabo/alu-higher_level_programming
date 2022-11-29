#!/usr/bin/python3
''' function that adds 2 integers '''


def add_integer(a, b=98):
    ''' 
    Args:
        a : this must be either an integer or float
        b : must be either an integer or float, if not 
            it takes it's current value of 98
    Returns
        integer: the addition of
    '''
    if type(a) == float or type(b) == float:
        a = int(a)
        b = int(b)

    if type(a) != int:
        raise TypeError("a must be an integer")
    if type(b) != int:
        raise TypeError("b must be an integer")
