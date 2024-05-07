# def func(i, n):
#     if i > n:
#         return
#     print(i)
#     func(i + 1, n)


# func(1, 9)


# ------------------------------------------------------------------------
# print("using back tracking")


def func(i, n):
    if i < 1:
        return
    func(i - 1, n)
    print(i)


func(9, 9)
