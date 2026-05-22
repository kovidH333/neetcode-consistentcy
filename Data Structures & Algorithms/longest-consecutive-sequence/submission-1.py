class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0: return 0
        nums.sort()
        ans = 1
        temp = 1
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                temp += 1
                ans = max(ans, temp)
            elif nums[i+1] - nums[i] == 0:
                continue
            else:
                temp = 1
        return ans
            