import re


def create_phone_number(n):
    n = "".join(map(str, n))
    print(n, len(n))

    phone_num_regex = re.compile(r"(\d{3})(\d{3})(\d{4})")

    mo = phone_num_regex.search(n)

    phone_number = '(' + mo.group(1) + ') ' + mo.group(2) + '-' + mo.group(3)

    return (phone_number)


create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1])
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
create_phone_number([0, 2, 3, 0, 5, 6, 0, 8, 9, 0])
create_phone_number([0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
