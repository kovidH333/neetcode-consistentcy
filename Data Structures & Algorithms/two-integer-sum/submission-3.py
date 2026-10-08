class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashset = {}
        for i in range(0,len(nums)):
            comp = target - nums[i]
            if comp in hashset:
                return [hashset[comp], i]
            else:
                hashset[nums[i]] = i
    
        