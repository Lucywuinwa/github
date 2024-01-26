import sys

my_ints = sys.argv[1:]


def newlist(new):
    new_list_int = [int(i) for i in new]
    new_condition = [var if var % 3 != 0 else var * 10 for var in new_list_int]
    return new_condition


print(newlist(my_ints))
