"""Write an algorithm that takes an array and moves all of the zeros to
the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]"""


def move_zeros(array):
    num_zeros = array.count(0)
    new_list = []

    for x in array:
        if x is not 0:
            new_list.append(x)
    for y in range(num_zeros):
        new_list.append(0)
    return new_list

print()
print("===Basic tests===")
print()
print ('1 ', move_zeros([1, 2, 0, 1, 0, 1, 0, 3, 0, 1]) == [1, 2, 1, 1, 3, 1, 0, 0, 0, 0])

print ('2 ', move_zeros([9, 0.0, 0, 9, 1, 2, 0, 1, 0, 1, 0.0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) ==
        [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print ('3 ', move_zeros(["a", 0, 0, "b", "c", "d", 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9]) ==
        ["a", "b", "c", "d", 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print ('4 ',move_zeros(["a", 0, 0, "b", None, "c", "d", 0, 1, False, 0, 1, 0, 3, [], 0, 1, 9, 0, 0, {}, 0, 0, 9]) ==
        ["a", "b", None, "c", "d", 1, False, 1, 3, [], 1, 9, {}, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

print ('5 ',move_zeros([0, 1, None, 2, False, 1, 0]) == [1, None, 2, False, 1, 0, 0])
print ('6 ', move_zeros(["a", "b"]) == ["a", "b"])
print ('7 ', move_zeros(["a"]) == ["a"])
print ('8 ', move_zeros([0, 0]) == [0, 0])
print ('9 ', move_zeros([0]) == [0])
print ('10', move_zeros([]) == [])
