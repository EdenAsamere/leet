class Solution:
    def isPalindrome(self, s: str) -> bool:
        n =''
        for i in s:
            if i.isalnum():
                n+=i
        t =n.upper()
        if t == t[::-1]:
            return 'true'
        