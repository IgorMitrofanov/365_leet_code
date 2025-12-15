"""
Given a string s, find the length of the longest substring without duplicate characters.

 

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3. Note that "bca" and "cab" are also correct answers.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.
 

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""


"""
записывааем индекс начала подстроки - l, ответ (сначала равным нулю) - длина макс подстроки
и множество встреченых букв в подстроке - seen
идем слева направо, если символа еще нет в seen, гладем его туда и записываем ans 
если есть в seen, то пока он в seen, выкидываем от туда символы с l, увеличивая l каждый раз на 1
в конце добавляем символ в seen, новый символ, т.к. старый выкинули

"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        ans = 0
        seen = set()
        for r in range(len(s)):
            c = s[r]
            if c not in seen:
                seen.add(c)
                ans = max(ans, r - l + 1)
            else:
                while c in seen:
                    seen.remove(s[l])
                    l += 1
                seen.add(c)
                ans = max(ans, r - l + 1)
        return ans

