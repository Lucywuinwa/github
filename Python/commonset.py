import sys 
set_a = sys.argv[1:]
set_b = ['apple', 'banana', 'mango', 'orange']

#def common (fruit):
#    fruit = sys.argv[1]
#    result = [ set(set_a) & set(set_b)}]
#print(common)

def common_fruit(set_a, set_b):
    set_a = set(set_a)
    set_b = set(set_b)
    return set_a & set_b

print(common_fruit(set_a, set_b)) 