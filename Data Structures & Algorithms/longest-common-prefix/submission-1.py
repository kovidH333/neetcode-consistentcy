class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        # # 1.bruteforce
        # minsize = len(strs[0])
        # for s in strs:
        #     minsize = min(minsize,len(s))

        # i=0
        # ans = ""
        # while(i<minsize):
        #     for j in range(1,len(strs)):
        #         if strs[j-1][i] == strs[j][i]:
        #             continue
        #         else:
        #             return ans
        #     ans += strs[0][i]
        #     i += 1     
        
        # return ans

        # 2.optimal
        strs.sort()
        ans = ""
        for j in range(min(len(strs[0]),len(strs[-1]))):
                if strs[0][j] == strs[-1][j]:
                    ans += strs[0][j]
                else:
                    return ans
        return ans
            
