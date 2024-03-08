'''

Consecutive zeros
The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.

'''

def consecutive_zeros(strParam):
    result = 0
    count = 0
    for num in list(strParam):
        if num == '0':
            count += 1
        elif num == '1':
            if count > result:
                result = count 
            count = 0
        
    return result


print(consecutive_zeros("1001101000110"))