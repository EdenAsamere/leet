class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        intial = []
        for i in range(len(nums)+1):
            intial.append(i)
        set1 = set(nums)
        set2 = set(intial)
        difference = set2 - set1
        return difference.pop()
        