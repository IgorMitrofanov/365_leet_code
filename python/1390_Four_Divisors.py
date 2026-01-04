"""
Given an integer array nums, return the sum of divisors of the integers in that array that have exactly four divisors. If there is no such integer in the array, return 0.

 

Example 1:

Input: nums = [21,4,7]
Output: 32
Explanation: 
21 has 4 divisors: 1, 3, 7, 21
4 has 3 divisors: 1, 2, 4
7 has 2 divisors: 1, 7
The answer is the sum of divisors of 21 only.

Example 2:

Input: nums = [21,21]
Output: 64

Example 3:

Input: nums = [1,2,3,4,5]
Output: 0
 

Constraints:

1 <= nums.length <= 104
1 <= nums[i] <= 105
"""

class Solution:
    def sumFourDivisors(self, nums: List[int]) -> int:
        def is_prime(x: int) -> bool:
            if x < 2:
                return False
            for d in range(2, int(x**.5) + 1):
                if x % d == 0:
                    return False
            return True

        result = 0
        for num in nums:
            for p in range(2, int(num**.5) + 1):
                if num % p == 0:
                    q = num // p
                    if q == p:
                        break
                    else:
                        if num == p**3 and is_prime(p):
                            result += 1 + p + p**2 + p**3
                        elif is_prime(p) and is_prime(q):
                            result += 1 + p + q + num
                        break
        return result

                    