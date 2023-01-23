#!/usr/bin/python3


def list_division(my_list_1, my_list_2, list_length):
    newL = []
    for i in range(list_length):
        try:
            newL.append(my_list_1[i] / my_list_2[i])
        except TypeError:
            print("wrong type")
            newL.append(0)
        except ZeroDivisionError:
            print("division by 0")
            newL.append(0)
        except IndexError:
            print("out of range")
            newL.append(0)
        finally:
            pass
    return newL
