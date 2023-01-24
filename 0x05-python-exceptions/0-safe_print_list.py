#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    loop = 0;
    for pr in range(x):
        try:
            print("{}".format(my_list[pr]), end='')
            loop = loop + 1
        except IndexError:
            break
    print("")
    return loop
