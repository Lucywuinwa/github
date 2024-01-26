import sys

set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']

def differ_fruit(set_a, set_b):
    set_a = set(set_a)
    set_b = set(set_b)
    return set_a .difference (set_b)
    
print(differ_fruit(set_a, set_b))