"""Write an algorithm that takes an array and moves all of the zeros to
the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]"""


def move_zeros(array):
    num_zeros = array.count(0)
    print(num_zeros)
    new_list = []

    for x in array:
        if x is not 0:
            new_list.append(x)
    for y in range(num_zeros):
        new_list.append(0)
    return new_list

print(move_zeros(["a",0,0,"b",None,"c","d",0,1,False,0,1,0,3,[],0,1,9,0,0,{},0,0,9]))
print(["a","b",None,"c","d",1,False,1,3,[],1,9,{},9,0,0,0,0,0,0,0,0,0,0])