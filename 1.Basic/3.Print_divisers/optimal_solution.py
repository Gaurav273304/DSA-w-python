"""
Time complexity = O(n) where n is the number
space complexity = O(d) where n is the number of divisors of the input integer n
"""

from typing import List
from math import sqrt


def divisors(num: int) -> List:
    divisor_list = []
    for i in range(1, int(num**0.5) + 1):
        if num % i == 0:
            divisor_list.append(i)
            if i != num // i:
                divisor_list.append(num // i)
    divisor_list.sort()
    return divisor_list


print(divisors(23))
