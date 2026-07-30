class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        while left < right:
            middle = int((left + right) / 2)
            if nums[left] > nums[right]:
                if nums[middle] > nums[right] and left != middle:
                    left = middle
                elif left == middle:
                    left = middle + 1
                else:
                    right = middle
            else:
                return nums[left]
        return nums[left]
