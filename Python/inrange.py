import sys


def filtered_print_all(divisor):
    divisor = int(divisor)
    result = []
    for i in range(3000, 5000):
        if i % divisor == 0 and i % (divisor + 7) == 0 and i % (divisor * divisor) == 0:
            result.append(i)
    return result



print(filtered_print_all(sys.argv[1]))
