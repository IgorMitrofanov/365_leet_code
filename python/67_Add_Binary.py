"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
 

Constraints:

1 <= a.length, b.length <= 104
a and b consist only of '0' or '1' characters.
Each string does not contain leading zeros except for the zero itself.
"""

"""
задаю пустой список result для хранения результата и переменную carry для хранения переноса
задаю указатели i и j для конца строк a и b соответственно
делаю цикл, который продолжается, пока i или j не меньше 0 или есть перенос
    задаю переменную sum, равную carry
    если i не меньше 0, добавляю значение a[i] к sum и уменьшаю i на 1
    если j не меньше 0, добавляю значение b[j] к sum и уменьшаю j на 1
    добавляю в result строковое представление sum % 2 (остаток от деления на 2)
    обновляю carry как sum // 2 (целочисленное деление на 2)
в конце возвращаю объединение перевернутого списка result в строку

"""


class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = []
        carry = 0
        i, j = len(a) - 1, len(b) - 1
        
        while i >= 0 or j >= 0 or carry:
            sum = carry
            
            if i >= 0:
                sum += int(a[i])
                i -= 1
            if j >= 0:
                sum += int(b[j])
                j -= 1
            
            result.append(str(sum % 2))
            carry = sum // 2
        
        return ''.join(reversed(result))