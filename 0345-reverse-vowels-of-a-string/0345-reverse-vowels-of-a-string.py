class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        l, r = 0, len(s)-1
        slist = list(s)
        while l < r:
            if slist[l] not in vowels:
                l+=1
            if slist[r] not in vowels:
                r-=1
            if slist[l] in vowels and slist[r] in vowels:
                slist[l],slist[r]= slist[r],slist[l]
                l+=1
                r-=1
        return ''.join(slist)
                
                    
        