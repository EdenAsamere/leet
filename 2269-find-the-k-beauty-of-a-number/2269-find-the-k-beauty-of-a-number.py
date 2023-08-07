class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        count = 0
        nums = str(num)
        for i in range(len(nums)-k+1):
            substring = int(nums[i:i+k])
            if substring != 0 and num % substring == 0:
                count += 1
        return count
