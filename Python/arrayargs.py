# Create a program called arrayargs.py that has a function that takes four
# integer arguments. Those arguments should be put into an Numpy array.

# The function will have two print statements.
# The first will print the type of the array you create (which should be
# <class ‘numpy.ndarray’>).
# For this, DO NOT just do print(“<class ‘numpy.ndarray’>”)
# The second will print the multiplication of the four items in your array.

# Your output could look like this (it could differ in parts):
# 	<class ‘numpy.ndarray’>
# 	80


import sys

import numpy as np


def print_stuff(a, b, c, d):
    numpy_array = np.array([int(a), int(b), int(c), int(d)])
    print(type(numpy_array))

    product = numpy_array.prod()
    print(product)



print_stuff(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])