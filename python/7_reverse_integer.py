"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321

Example 2:

Input: x = -123
Output: -321

Example 3:

Input: x = 120
Output: 21
 

Constraints:

-231 <= x <= 231 - 1
"""

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        res = 0
        INT32_MAX = 2**31 - 1
        INT32_MIN = -2**31
        ax = abs(x)
        sign = -1 if x < 0 else 1 
        while ax != 0 :
            digit = ax % 10
            ax = ax // 10
            limit = INT32_MAX if sign == 1 else -INT32_MIN
            if (res > limit // 10) or (res == limit // 10 and digit > limit % 10):
                return 0
            res = res * 10 + digit
        return sign * res