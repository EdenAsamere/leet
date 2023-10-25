class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)          
        windowSum = sum(nums[:k])
        maxAverage = windowSum/k
        for i in range(n-k):
            windowSum = windowSum - nums[i] + nums[i+k]
            windowAverage = windowSum/k
            maxAverage = max(maxAverage,windowAverage)
        return maxAverage  