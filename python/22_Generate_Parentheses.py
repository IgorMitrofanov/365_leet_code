"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

 

Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
 

Constraints:

1 <= n <= 8
"""

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(s: str, open_used: int, close_used: int):
            if len(s) == 2 * n:
                res.append(s)
                return

            if open_used < n:
                backtrack(s + "(", open_used + 1, close_used)

            if close_used < open_used:
                backtrack(s + ")", open_used, close_used + 1)

        backtrack("", 0, 0)
        return res
