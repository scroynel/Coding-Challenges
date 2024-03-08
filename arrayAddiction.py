'''

Have the function ArrayAdditionI(arr) take the array of numbers stored in arr 
and return the string true if any combination of numbers in the array can be 
added up to equal the largest number in the array, otherwise return the string 
false. For example: if arr contains [4, 6, 23, 10, 1, 3] the output should 
return true because 4 + 6 + 10 + 3 = 23. The array will not be empty, will not 
contain all the same elements, and may contain negative numbers.

Examples:

Input: [5, 7, 16, 1, 2]
Output: false

Input: [3, 5, -1, 8, 12]
Output: true

'''
# Way 1
from itertools import combinations

def ArrayAddictionI(numbers):
    expected_sum = max(numbers)
    numbers.remove(expected_sum)
    print(numbers)

    result = []
    
    for i in range(len(numbers), 0, -1):
        for seq in combinations(numbers, i):
            if sum(seq) == expected_sum:
                result.append(seq)

    print(result)
    return len(result) > 0


print(ArrayAddictionI([30, 9, 111, 2, 70, 25, 46]))
print(ArrayAddictionI([4, 6, 23, 10, 1, 3]))
