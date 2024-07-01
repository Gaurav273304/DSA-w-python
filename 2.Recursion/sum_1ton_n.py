def sum1ton(n):
    if n == 1:
        return 1
    return n +  sum1ton(n-1)

print(sum1ton(4))