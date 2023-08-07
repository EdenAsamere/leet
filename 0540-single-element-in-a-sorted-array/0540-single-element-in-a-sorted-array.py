class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0 
        j = len(nums)-1
        while i < j:
            if i< j and nums[i] !=nums[i+1]:
                return nums[i]
            if i< j and nums[j]  != nums[j-1]:
                return nums[j]
            j-=2
            i+=2
        return nums[i]
        