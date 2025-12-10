"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
 

Example 1:

Input: s = "()"

Output: true

Example 2:

Input: s = "()[]{}"

Output: true

Example 3:

Input: s = "(]"

Output: false

Example 4:

Input: s = "([])"

Output: true

Example 5:

Input: s = "([)]"

Output: false

 

Constraints:

1 <= s.length <= 104
s consists of parentheses only '()[]{}'.
"""

"""
создаем мапу с парами скобок
создаем стек
проходимся по каждому символу,
если встречена открывающая скобка, кладем ее в стек, 
если встречена соответствующая ей закрывающая, проверяем
если стек пустой, или она не соответствует вершине стека - Фолс, в ином случае - выкидываем из стека

инвариант: после обработки первых k символов, строка валидна пока что, и:
стек содержит только открывающие скобки, которые еще не закрыты
порядок в стеке соответствует ожидаемому порядку закрытия, последняя должна закрыться первой
"""


class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        char_map = {
            "(" : ")",
            "[" : "]",
            "{" : "}"
        }
        stack = []
        for char in s:
            if char in char_map:
                stack.append(char)
            else:
                if not stack or char_map[stack[-1]] != char:
                    return False
                else:
                    stack.pop()
        return not stack

sol = Solution()
assert sol.isValid("()") is True
assert sol.isValid("()[]{}") is True
assert sol.isValid("([])") is True
assert sol.isValid("(]") is False
assert sol.isValid("([)]") is False
assert sol.isValid("]") is False
assert sol.isValid("(((") is False
