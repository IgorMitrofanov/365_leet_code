"""
Given a non-negative integer x, return the square root of x rounded down to the nearest integer. The returned integer should be non-negative as well.

You must not use any built-in exponent function or operator.

For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.
 

Example 1:

Input: x = 4
Output: 2
Explanation: The square root of 4 is 2, so we return 2.

Example 2:

Input: x = 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since we round it down to the nearest integer, 2 is returned.
 

Constraints:

0 <= x <= 231 - 1

"""


"""
создам указатель left и right для бинарного поиска
пока left меньше или равно right, вычисляю mid как среднее значение между left и right
умножаю mid на себя, чтобы получить его квадрат
если квадрат равен x, возвращаю mid
если квадрат меньше x, сдвигаю left вправо (left = mid + 1)
если квадрат больше x, сдвигаю right влево (right = mid - 1)
в конце возвращаю right, так как он будет указывать на наибольшее целое число, квадрат которого меньше или равен x
    
"""


class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        
        left, right = 2, x // 2
        
        while left <= right:
            mid = left + (right - left) // 2
            squared = mid * mid
            
            if squared == x:
                return mid
            elif squared < x:
                left = mid + 1
            else:
                right = mid - 1
        
        return right