"""Write an algorithm that takes an array and moves all of the zeros to
the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]"""

import unittest as Test


def move_zeros(array):
    new_list = []
    num_zeros = 0

    for x in array:
        # print(x, x is not 0, x is not 0.0)
        if x == 0 and x is not False:
            num_zeros += 1
        else:
            new_list.append(x)
    for y in range(num_zeros):
        new_list.append(0)
    return new_list

