class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        minVal = nums[0]

        while low <= high:
            if nums[low] < nums[high]:
                minVal = min(minVal, nums[low])
                break
            
            middle = (low + high) // 2
            minVal = min(minVal, nums[middle])

            if nums[middle] >= nums[low]:
                low = middle + 1
            else:
                high = middle - 1
        return minVal  


           

        