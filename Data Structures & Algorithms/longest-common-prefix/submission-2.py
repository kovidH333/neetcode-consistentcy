class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        l = len(strs[0])
        ans = ""
        for str in strs:
            l = min(l,len(str))
        for i in range(0,l):
            for str in strs:
                if str[i] != strs[0][i]:
                    return ans
            ans += strs[0][i]
        return ans