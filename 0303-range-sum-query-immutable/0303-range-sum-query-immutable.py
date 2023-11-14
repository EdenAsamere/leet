class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums       

    def sumRange(self, left: int, right: int) -> int:
        prefix = 0
        for i in range(left,right+1):
            prefix += self.nums[i]
        return prefix
            
            
        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)