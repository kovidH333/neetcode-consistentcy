class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        temp = 1
        ans = nums[0]
        for i in range(len(nums)-1):
            if nums[i+1] == nums[i]:
                temp += 1
                if temp > len(nums)/2:
                    return ans
            else: 
                ans = nums[i+1]
                temp = 1
        
        return ans