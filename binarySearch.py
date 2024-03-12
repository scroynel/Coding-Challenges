'''

Binary search

'''


def binary_search(nums, target):
    nums.sort()
    low = 0
    high = len(nums) - 1

    while low <= high:
        mid = (low + high) // 2
        if nums[mid] == target:
            return mid
        else:
            if nums[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
    return None

print(binary_search([80, 70, 50, 55, 75, 89, 78, 34, 56, 67, 31, 33, 1, 5, 9, 7, 56], 67))