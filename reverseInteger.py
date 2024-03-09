'''

Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21

'''

# WAY 1
def reverse(x):
    MAX = 2 ** 31 - 1
    MIN = -2 ** 31
    result = []
    list_num = list(str(x))

    if '-' in list_num:
        result.append(list_num[0])
        result.extend(list_num[1:][::-1])
    else:
        result = list_num[::-1]
    
    number = int(''.join(result))
    if number > MAX or number < MIN:
        return 0 
    
    return number


# WAY 2
def reverse(x):
    MAX = 2 ** 31 -1
    MIN = -2 ** 31

    reversed_num = 0
    negative = False
    if x < 0:
        x = -x
        negative = True

    while x > 0:
        last_digit = x % 10
        reversed_num = reversed_num * 10 + last_digit
        x = x // 10

    if negative:
        reversed_num *= -1

    if reversed_num < MIN or reversed_num > MAX:
        return 0

    return reversed_num

print(reverse(123))
print(reverse(-578))
print(reverse(1534236469))