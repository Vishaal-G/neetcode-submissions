class Solution:
    def jump(self, nums: List[int]) -> int:
        count = 0
        left = right = 0
        
        while right < len(nums) - 1:
            maxJump = 0
            for i in range (left, right + 1):
                maxJump = max(maxJump, i + nums[i])
            count += 1
            left = right + 1
            right = maxJump

        return count
            
            

            



        