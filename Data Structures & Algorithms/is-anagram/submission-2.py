class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
    # #direct_sort
    #     ss = "".join(sorted(s))
    #     st = "".join(sorted(t))
    #     return ss==st

    # #hashmap
    #     if len(s) != len(t):
    #         return False
        
    #     hashmap = {}

    #     for char in s:
    #         hashmap[char] = hashmap.get(char, 0) + 1

    #     for char in t:
    #         if char not in hashmap:
    #             return False
    #         hashmap[char] -= 1
    #         if hashmap[char] == 0:
    #             del hashmap[char]

    #     return not hashmap

    #hasharray

        if len(s) != len(t):
            return False
        
        hasharray = [0]*26

        for char in s:
            hasharray[ord(char)-ord('a')] += 1
        for char in t:
            hasharray[ord(char)-ord('a')] -= 1
            
        for val in hasharray:
            if val != 0:
                return False
        
        return True

    

