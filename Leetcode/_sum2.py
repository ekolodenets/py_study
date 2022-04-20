#find numbers of sums (only with ordered list!!!)
def twoSum(nums, target):
    l = 0
    r = len(nums) - 1
    while l < r:
        sum = nums[l] + nums[r]
        if sum == target:
            print([nums[l], nums[r]])
            return [nums[l], nums[r]]
        if sum < target:
            l += 1
        else:
            r -= 1
    return []

assert twoSum([-3, 0, 1, 3, 4], 5) == [1, 4]

