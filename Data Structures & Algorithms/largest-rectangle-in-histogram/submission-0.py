class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = [(0, -1)]  
        max_area = 0
        n = len(heights)

        for i in range(n + 1):  
            curr = heights[i] if i < n else 0
            while stack and stack[-1][0] > curr:
                height, index = stack.pop()
                left_smaller_idx = stack[-1][1]
                width = i - left_smaller_idx - 1
                max_area = max(max_area, height * width)
            stack.append((curr, i))

        return max_area



            
                

            
            