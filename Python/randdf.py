# randdf.py
# Create a program called randdf.py
# that has a function that takes two integer arguments and
# prints a Pandas dataframe.
#  The two arguments will correspond to the number of rows and number of columns,
#  respectively.  The dataframe should be filled with random integers from 0 to 100.

# Set your numpy random seed to 56.
# Note: Use random from numpy. Otherwise, you might get a different result.

import sys

import numpy as np
import pandas as pd
import pandas as pd


def randdf(a: int, b: int) -> pd.DataFrame:
    np.random.seed(56)
    df = pd.DataFrame(np.random.randint(low=0, high=100, size=[a, b]))
    return df


print(randdf(int(sys.argv[1]), int(sys.argv[2])))
