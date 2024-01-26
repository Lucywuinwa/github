import sys
loop_list = sys.argv[1:]

def newlist(new):
    new_list_int = [int(i) for i in new]
    return [i + x for i, x in enumerate(new_list_int)]



print(newlist(loop_list))

