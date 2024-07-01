def power(b,e):
    if e == 1:
        return b
    elif e == 0:
        return 1
    return b * power(b,e-1)

print(power(2,3))
