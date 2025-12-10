"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

For example, 2 is written as II in Roman numeral, just two ones added together. 12 is written as XII, 
which is simply X + II. The number 27 is written as XXVII, which is XX + V + II.

Roman numerals are usually written largest to smallest from left to right. However, 
the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:

I can be placed before V (5) and X (10) to make 4 and 9. 

X can be placed before L (50) and C (100) to make 40 and 90. 

C can be placed before D (500) and M (1000) to make 400 and 900.

Given a roman numeral, convert it to an integer.

Example 1:

Input: s = "III"
Output: 3
Explanation: III = 3.

Example 2:

Input: s = "LVIII"
Output: 58
Explanation: L = 50, V= 5, III = 3.

Example 3:

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

"""

"""
Делаем мапу романские-целые, для быстрого поиска целого числа по романскому. 
инициализиурем переменную-сумму и делаем указатель на первый символ
далее в цикле проверяем, если предыдущий символ меньше чем следующий,
то делаем вытчитание от переменной суммы, если больше или равно - сложение
после цикла суммируем последний символ, так как у него нет следующего
"""

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return None
        roman_numbers_map = {
            "I" : 1,
            "V" : 5,
            "X" : 10,
            "L" : 50,
            "C" : 100,
            "D" : 500,
            "M" : 1000
        }
        int_num = 0
        prev_char = s[0]
        for char in s[1:]:
            prev_int = roman_numbers_map[prev_char]
            next_int = roman_numbers_map[char]
            if prev_int < next_int:
                int_num -= prev_int
            else:
                int_num += prev_int
            prev_char = char
        int_num += roman_numbers_map[prev_char]
        return int_num


sol = Solution()

# Простые сложения
assert sol.romanToInt("I") == 1
assert sol.romanToInt("III") == 3
assert sol.romanToInt("VIII") == 8
assert sol.romanToInt("LVIII") == 58  # 50 + 5 + 3

# Все 6 вычитательных пар
assert sol.romanToInt("IV") == 4
assert sol.romanToInt("IX") == 9
assert sol.romanToInt("XL") == 40
assert sol.romanToInt("XC") == 90
assert sol.romanToInt("CD") == 400
assert sol.romanToInt("CM") == 900

# Смешанные классические примеры
assert sol.romanToInt("MCMXCIV") == 1994
assert sol.romanToInt("MMXXIII") == 2023
assert sol.romanToInt("XLII") == 42      # 40 + 2
assert sol.romanToInt("XCIX") == 99      # 90 + 9
assert sol.romanToInt("CDXLIV") == 444   # 400 + 40 + 4
assert sol.romanToInt("CMXC") == 990     # 900 + 90

# Верхняя граница (обычно в задаче 1..3999)
assert sol.romanToInt("MMMCMXCIX") == 3999
