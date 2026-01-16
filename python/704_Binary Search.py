from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            
            if left == right:
                break
            
            elif nums[mid] < target:
                # right side
                left = mid + 1
            else:
                # left side
                right = mid - 1 
        return mid if nums[mid] > target else mid + 1


nums = [1,3]
target = 2

sol = Solution()

print(sol.searchInsert(nums=nums, target=target))