class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        p = 1
        for num in nums:
            p = p*num
        ans = []
        for i in range(len(nums)):
            if nums[i] != 0:
                ans.append(p//nums[i])
            else:
                q = 1
                for j in range(len(nums)):
                    if j!=i:
                        q=q*nums[j]
                ans.append(q)
        return ans

                
        