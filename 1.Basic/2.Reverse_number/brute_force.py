"""
Time complexity = O(log10 n) where n is the digit
space complexity = O(1)
"""


def reverse_number(num: int) -> int:
    n = num
    reverse_num = 0
    while n != 0:
        digit = n % 10
        reverse_num = reverse_num * 10 + digit
        n //= 10
    return reverse_num


print(reverse_number(1234))
