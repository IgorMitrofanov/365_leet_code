"""
Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

 

Example 1:

Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.
Example 2:

Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
 

Constraints:

nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

class Solution(object):
    def quicksort(self, nums):
        if len(nums) <= 1:
            return nums
        else:
            q = random.choice(nums)
            s_nums = []
            m_nums = []
            e_nums = []
            for n in nums:
                if n < q:
                    s_nums.append(n)
                elif n > q:
                    m_nums.append(n)
                else:
                    e_nums.append(n)
            return self.quicksort(s_nums) + e_nums + self.quicksort(m_nums)

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        nums = nums1 + nums2
        # s_nums = self.quicksort(nums)
        s_nums = sorted(nums)

        n = len(s_nums)
        mid = n // 2

        if n % 2 == 0:
            return (s_nums[mid - 1] + s_nums[mid]) / 2.0
        else:
            return float(s_nums[mid])

    