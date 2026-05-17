# # 1.brute force
# class Solution:
#     def getConcatenation(self, nums: List[int]) -> List[int]:
#         n = len(nums)
#         ans = [0]*(2*n)
#         for i in range(0,2*n):
#             if i<n: ans[i]=nums[i]
#             else: ans[i]=nums[i-n]
#         return ans

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        # n = len(nums)
        # for i in range(n):
        #     nums.append(nums[i])
        # return nums

        ans = nums+nums
        return ans