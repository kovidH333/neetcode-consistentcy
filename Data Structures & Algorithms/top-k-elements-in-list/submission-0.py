class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        ans = []
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i],0) + 1
        freq = dict(sorted(freq.items(), key=lambda x:x[1], reverse=True))
        for key in freq:
            ans.append(key)
            k -= 1
            if k == 0:
                break

        return ans