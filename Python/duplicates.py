import sys

duplicated_words = sys.argv[1:]


def remove_dup(var):
    mylist = []
    for i in var:
        if i not in mylist:
            mylist.append(i)
    return mylist


print(sorted(remove_dup(sys.argv[1:]), reverse=True))
