class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        l , r = 0, len(height) -1
        while l < r:
            min_height = min(height[l],height[r])
            width = r - l
            area = width * min_height
            max_area = max(max_area,area)
            if min_height == height[l]: l +=1
            else: r-=1
        return max_area