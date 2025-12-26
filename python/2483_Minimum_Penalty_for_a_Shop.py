"""
You are given the customer visit log of a shop represented by a 0-indexed string customers consisting only of characters 'N' and 'Y':

if the ith character is 'Y', it means that customers come at the ith hour
whereas 'N' indicates that no customers come at the ith hour.
If the shop closes at the jth hour (0 <= j <= n), the penalty is calculated as follows:

For every hour when the shop is open and no customers come, the penalty increases by 1.
For every hour when the shop is closed and customers come, the penalty increases by 1.
Return the earliest hour at which the shop must be closed to incur a minimum penalty.

Note that if a shop closes at the jth hour, it means the shop is closed at the hour j.

 

Example 1:

Input: customers = "YYNY"
Output: 2
Explanation: 
- Closing the shop at the 0th hour incurs in 1+1+0+1 = 3 penalty.
- Closing the shop at the 1st hour incurs in 0+1+0+1 = 2 penalty.
- Closing the shop at the 2nd hour incurs in 0+0+0+1 = 1 penalty.
- Closing the shop at the 3rd hour incurs in 0+0+1+1 = 2 penalty.
- Closing the shop at the 4th hour incurs in 0+0+1+0 = 1 penalty.
Closing the shop at 2nd or 4th hour gives a minimum penalty. Since 2 is earlier, the optimal closing time is 2.
Example 2:

Input: customers = "NNNNN"
Output: 0
Explanation: It is best to close the shop at the 0th hour as no customers arrive.
Example 3:

Input: customers = "YYYY"
Output: 4
Explanation: It is best to close the shop at the 4th hour as customers arrive at each hour.
 

Constraints:

1 <= customers.length <= 105
customers consists only of characters 'Y' and 'N'.
"""

class Solution(object):
    def bestClosingTime(self, customers):
        """
        :type customers: str
        :rtype: int
        """
        n = len(customers)
    
        # 1. Считаем общее количество 'Y' в строке
        total_y = 0
        for ch in customers:
            if ch == 'Y':
                total_y += 1
        
        # 2. Инициализация
        min_penalty = float('inf')
        best_hour = 0
        count_y_so_far = 0  # сколько 'Y' уже прошли (слева от текущего j)
        
        # 3. Рассматриваем все возможные часы закрытия j от 0 до n включительно
        for j in range(n + 1):
            # Штрафы:
            # left_penalty = количество 'N' в первых j часах
            # но у нас есть только count_y_so_far для j первых часов
            # left_penalty = j - count_y_so_far  (всего часов j минус 'Y' в них)
            
            # right_penalty = количество 'Y' в оставшихся часах
            # = total_y - count_y_so_far
            
            # total_penalty = left_penalty + right_penalty
            left_penalty = j - count_y_so_far
            right_penalty = total_y - count_y_so_far
            penalty = left_penalty + right_penalty
            
            # 4. Обновляем минимум (ищем самый ранний час)
            if penalty < min_penalty:
                min_penalty = penalty
                best_hour = j
            
            # 5. Обновляем count_y_so_far для следующей итерации
            # Важно: делаем это ПОСЛЕ вычисления penalty для текущего j
            if j < n and customers[j] == 'Y':
                count_y_so_far += 1
        
        return best_hour