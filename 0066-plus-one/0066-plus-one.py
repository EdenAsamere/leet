class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 0
        count = len(digits)-1
        res =[]
        for i in range(len(digits)):
            dig = digits[i]
            num+=dig*10**count
            count-=1     
        for i in str(num+1):
            res.append(int(i))
        return res