class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1,nums2= nums[:n],nums[n:]
        temp = list(zip(nums1,nums2))
        ans = list(sum(temp,()))
        return ans


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        nums1,nums2= nums[:n],nums[n:]
        temp = list(zip(nums1,nums2))
        return [item for t in temp for item in t]
