class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet = set()
        l  = r = res = 0
        n = len(s)
        for r in range(n):
            while s[r] in charSet:
                charSet.remove(s[l])
                l+=1
            charSet.add(s[r])
            res = max(res,r-l+1)
        return res