class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minsize = len(strs[0])
        for s in strs:
            minsize = min(minsize,len(s))

        i=0
        ans = ""
        while(i<minsize):
            for j in range(1,len(strs)):
                if strs[j-1][i] == strs[j][i]:
                    continue
                else:
                    return ans
            ans += strs[0][i]
            i += 1     
        
        return ans