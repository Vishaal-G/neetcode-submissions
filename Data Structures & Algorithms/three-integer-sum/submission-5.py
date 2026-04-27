class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        tripletList = []

        for i in range(len(nums)):
            # Skip duplicates for the first number
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            l = i + 1
            r = len(nums) - 1
            temp = 0
            value = 0

            while l < r:
                if nums[l] + nums[r] + nums[i] > 0:
                    temp = r
                    value = nums[temp]
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    temp = l
                    value = nums[temp]
                    l += 1
                else:
                    tripletList.append([nums[i], nums[l], nums[r]])

                    # Move both pointers & skip duplicates
                    left_val = nums[l]
                    right_val = nums[r]
                    while l < r and nums[l] == left_val:
                        l += 1
                    while l < r and nums[r] == right_val:
                        r -= 1

        return tripletList
