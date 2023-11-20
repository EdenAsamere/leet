class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict,tdict = {},{}
        for c in s:
            if c in sdict:
                sdict[c]+=1
            else:
                sdict[c]=1
        for c in t:
            if c in tdict:
                tdict[c]+=1
            else:
                tdict[c]=1
        return sdict == tdict
                