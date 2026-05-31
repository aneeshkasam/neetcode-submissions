class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        helper = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in helper:
                return [helper[diff], i]

            helper[num] = i