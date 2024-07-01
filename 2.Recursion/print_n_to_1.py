# def func(n):
#     if n < 1:
#         return
#     print(n)
#     func(n-1)


# func(9,)

# -----------------------------------------------------------------

def func(i, n):
    if i < n:
        return
    print(i)
    func(i - 1, n)


func(7,4)