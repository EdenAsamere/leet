class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        dic ={}
        for i in nums:
            if i not in dic:
                dic[i] =1
            else:
                dic[i]+=1
        for i,j in dic.items():
            if j> len(nums)//2:
                return i
        