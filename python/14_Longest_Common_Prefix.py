"""
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".

 

Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
 

Constraints:

1 <= strs.length <= 200
0 <= strs[i].length <= 200
strs[i] consists of only lowercase English letters if it is non-empty.
"""

"""
берем первую строку полностью как префикс-кандидат (pref), далее для каждой следующей:
если строка не начинается с pref, укорачиваем его на 1 символ с конца, если он стал пустым - ответ ""
"""

class Solution(object):
    def longestCommonPrefix(self, strs: list[str]):
        """
        :type strs: List[str]
        :rtype: str
        """
        if not len(strs) >= 1:
            return strs[0]
        pref = strs[0]
        for s in strs[1:]:
            while not s.startswith(pref):
                pref = pref[:-1]
                if not pref:
                    return pref
        return pref

sol = Solution()

# Базовые примеры
assert sol.longestCommonPrefix(["flower", "flow", "flight"]) == "fl"
assert sol.longestCommonPrefix(["dog", "racecar", "car"]) == ""

# Один элемент
assert sol.longestCommonPrefix(["abc"]) == "abc"

# Есть пустая строка
assert sol.longestCommonPrefix(["", "abc"]) == ""
assert sol.longestCommonPrefix(["abc", ""]) == ""
assert sol.longestCommonPrefix(["", ""]) == ""

# Все одинаковые
assert sol.longestCommonPrefix(["test", "test", "test"]) == "test"

# Полный префикс — это самая короткая строка
assert sol.longestCommonPrefix(["ab", "ab", "abx"]) == "ab"

# Префикс длины 1
assert sol.longestCommonPrefix(["a", "ab", "ac"]) == "a"

# Нет общего префикса вообще
assert sol.longestCommonPrefix(["a", "b", "c"]) == ""

# Общий префикс обрывается на середине
assert sol.longestCommonPrefix(["interspecies", "interstellar", "interstate"]) == "inters"

# Частый tricky: первая строка длиннее остальных
assert sol.longestCommonPrefix(["aaaa", "aa", "aaa"]) == "aa"
