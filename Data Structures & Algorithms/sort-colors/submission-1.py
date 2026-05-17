# # 1. brute force
# class Solution:
#     def sortColors(self, nums: List[int]) -> None:
#         """
#         Do not return anything, modify nums in-place instead.
#         """
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] > nums[j]:
#                     temp = nums[i]
#                     nums[i] = nums[j]
#                     nums[j] = temp

# 2.optimal
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        a = b = c = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                a += 1
            elif nums[i] == 1:
                b += 1
            else:
                c += 1
        for i in range(len(nums)):
            if a>0:
                nums[i] = 0
                a -= 1
            elif b>0:
                nums[i] = 1
                b -= 1
            else:
                nums[i] = 2
        
        
        