from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # [2, 3, 1, 1, 4]
        target_index = len(nums) - 1
        for index in range(target_index, -1, -1):
            if nums[index] >= target_index - index:
                target_index = index
        return target_index == 0
