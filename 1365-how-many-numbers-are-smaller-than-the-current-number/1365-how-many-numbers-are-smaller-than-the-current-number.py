import functools
class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        dic = {}
        sorted_nums = sorted(nums)
        for i,j in enumerate(sorted_nums):
            if j not in dic:
                dic[j] = i
        print(dic)
        return [dic[i] for i in nums]
        