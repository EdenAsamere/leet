class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        i = 0
        j = len(nums)-1
        while i < j:
            mid = i+(j-i)//2
            if mid % 2 == 1:
                if nums[mid] == nums[mid-1]:
                    i = mid+1
                else:
                    j = mid-1
            else:
                if nums[mid] == nums[mid+1]:
                    i = mid+1
                else:
                    j = mid
        return nums[i]
