"""
Given an integer x, return true if x is a palindrome, and false otherwise.

 

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.

Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.

Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?

"""

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        def reverse(x):
            res = 0
            INT32_MAX = 2**31 - 1
            INT32_MIN = -2**31
            ax = abs(x)
            sign = -1 if x < 0 else 1
            while ax != 0:
                digit = ax % 10
                ax = ax // 10
                limit = INT32_MAX if sign == 1 else -INT32_MIN
                if (res > limit // 10) or (res == limit // 10 and digit > limit % 10):
                    return 0
                res = res*10 + digit
            return res
        print(x)
        print(reverse(x))
        return x == reverse(x)

sol = Solution() 

assert sol.isPalindrome(121) == True
assert sol.isPalindrome(-121) == False
assert sol.isPalindrome(10) == False