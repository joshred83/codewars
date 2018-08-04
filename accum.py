def accum(s):
    s_list = [x for x in s]
    accum_list = []
    for idx, ch in enumerate(s_list):
        ch = ''.join([ch] * (idx + 1))
        ch = ch.capitalize()
        accum_list.append(ch)

    return '-'.join(accum_list)


print(accum('alskdfj'))
