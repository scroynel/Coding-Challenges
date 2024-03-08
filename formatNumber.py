'''

Thousands separator
Write a function named format_number that takes a non-negative number as its only parameter.

Your function should convert the number to a string and add commas as a thousands separator.

For example, calling format_number(1000000) should return "1,000,000".

'''

# Way 1
def format_number(param):
    return f"{param:,}"

# Way 2
def format_number(param):
    s = str(param)
    groups = []

    while s and s[-1].isdigit():
        groups.append(s[-3:])
        s = s[:-3]
    return ','.join(groups[::-1])

print(format_number(1000000))