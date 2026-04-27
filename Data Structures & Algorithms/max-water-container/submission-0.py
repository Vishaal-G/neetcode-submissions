class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        r = len(heights)-1
        
        area = (r-l) * min(heights[l],heights[r])
        while l < r:
            if (heights[l] >= heights[r]):
                area = max(area,(r-l) * min(heights[l],heights[r]))
                r -= 1
            elif (heights[l] < heights[r]):
                area = max(area,(r-l) * min(heights[l],heights[r]))
                l += 1
        return area
                





                
            


        