"""
Time complexity = O(log10 n) where n is the digit
space complexity = O(1)
"""


def count_digits(num: int) -> int:
    count = 0
    n = num
    while n > 0:
        count += 1
        n = n // 10  # if the given input keep dividing the TC will (log10 n)
    return count


print(count_digits(1234))
