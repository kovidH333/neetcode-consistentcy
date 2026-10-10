class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        pairs = []
        for word in strs:
            pairs.append(("".join(sorted(word)), word))
        
        pairs.sort()

        ans = []
        temp = [pairs[0][1]]
        for i in range(len(pairs)-1):
            if pairs[i+1][0] == pairs[i][0]:
                temp.append(pairs[i+1][1])
            else:
                ans.append(temp)
                temp = [pairs[i+1][1]]
        ans.append(temp)

        return ans
