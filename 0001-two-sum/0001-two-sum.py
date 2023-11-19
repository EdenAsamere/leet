class Solution:
    def twoSum(self, nums,target):
        hashmap = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap:
                return [i, hashmap[complement]]
            else:
                hashmap[nums[i]] = i
     