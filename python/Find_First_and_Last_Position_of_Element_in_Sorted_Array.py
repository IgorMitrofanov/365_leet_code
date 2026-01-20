"""
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]

Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]

Example 3:

Input: nums = [], target = 0
Output: [-1,-1]
 

Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109

"""

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def find_left_bord():
            left = 0
            right = len(nums)
            while left < right:
                mid = (left+right) // 2
                if nums[mid] >= target:
                    right = mid
                else:
                    left = mid + 1
            return left 
        def find_right_bord():
            left = 0
            right = len(nums)
            while left < right:
                mid = (left+right) // 2
                if nums[mid] > target:
                    right = mid
                else:
                    left = mid + 1
            return left - 1
        left_pos = find_left_bord()
        if left_pos >= len(nums) or nums[left_pos] != target:
            return [-1, -1]
        
        right_pos = find_right_bord()
        return [left_pos, right_pos]
        
