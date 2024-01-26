import sys

def char_frequency(str1):
    dict = {}
    for n in str1:
        keys = dict.keys()
        if n in keys:
            dict[n] += 1
        else:
            dict[n] = 1
    return dict

print(char_frequency(sys.argv[1]))
#https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-2.php