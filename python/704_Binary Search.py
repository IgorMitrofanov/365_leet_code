from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        found_idx = -1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                found_idx = mid
                break
            elif nums[mid] < target:
                # right side
                left = mid + 1
            else:
                # left side
                right = mid - 1 
        return found_idx

nums = [-1, 0, 3, 5, 9, 12]
target = 9

sol = Solution()

print(sol.search(nums=nums, target=target))