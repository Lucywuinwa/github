import sys
from unittest import result

import numpy as np



def really_random(pool_size: int, multiply_coefficient: int, selection: int) -> int:
    if selection > pool_size: 
        print("")
    else:
        np.random.seed(42)
        pool = np.random.randint(low=0, high=10, size=(pool_size,))
        selected_num = pool[selection]
        result = multiply_coefficient * selected_num
        return result
 
result = really_random(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv[3]))
if int(sys.argv[3]) > int(sys.argv[1]): 
        print("")
else:    
    print(f"Your random value is {result}")
