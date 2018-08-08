class Solution(object):
    def searchInsert(self, nums, target):
        index = 0
        while index <= len(nums) - 1 and target > nums[index]:
            index = index + 1
        return index
nums = [1, 2, 3, 4]
target = 8
ans = Solution().searchInsert(nums, target)
print ans