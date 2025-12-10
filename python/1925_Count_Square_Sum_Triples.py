"""
A square triple (a,b,c) is a triple where a, b, and c are integers and a2 + b2 = c2.

Given an integer n, return the number of square triples such that 1 <= a, b, c <= n.

 

Example 1:

Input: n = 5
Output: 2
Explanation: The square triples are (3,4,5) and (4,3,5).

Example 2:

Input: n = 10
Output: 4
Explanation: The square triples are (3,4,5), (4,3,5), (6,8,10), and (8,6,10).

"""

"""
Сколько пар (a,b) дадут сумму c^2, т.е. для каждого c нужно посчитать кол-во решений a^2+b^2=c^2.

сделаем множество всех квадратов от 1 до n

для фиксированных a и c проверяем b:

b^2 = c^2 - a^2
"""

class Solution(object):
    def countTriples(self, n):
        """
        :type n: int
        :rtype: int
        """
        set_of_squares = set()
        count = 0
        for num in range(n+1):
            set_of_squares.add(num**2)

        for c in range(1, n+1):
            for a in range(1, c):
                if (c**2 - a**2) in set_of_squares:
                    count += 1
        return count
        

solution = Solution()
assert solution.countTriples(5) == 2
assert solution.countTriples(10) == 4