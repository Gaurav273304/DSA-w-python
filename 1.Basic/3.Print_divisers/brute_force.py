"""
Time complexity = O(n) where n is the number
space complexity = O(d) where n is the number of divisors of the input integer n
"""

from typing import List


def divisors(num: int) -> List:
    divisor_list = []
    for i in range(1, num + 1):
        if num % i == 0:
            divisor_list.append(i)
    return divisor_list


print(divisors(23))
