"""Write Number in Expanded Form
You will be given a number and you will need to return it as a string in Expanded Form. For example:

expanded_form(12) # Should return '10 + 2'
expanded_form(42) # Should return '40 + 2'
expanded_form(70304) # Should return '70000 + 300 + 4'
NOTE: All numbers will be whole numbers greater than 0."""


def expanded_form(num):
    subtract = 0
    expanded = []
    for divisor, factor in enumerate(reversed((range(0, len(str(num)))))):
        new_num = (num // 10 ** factor) * (10 ** factor) - subtract
        if new_num != 0:
            expanded.append(new_num)
        subtract += new_num

    string = ' + '.join(str(x) for x in expanded)
    return string

print(expanded_form(23904))
