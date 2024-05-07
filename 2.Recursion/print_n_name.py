def func(m: int, n: int):
    if m > n:
        return
    print("Gaurav")
    func(m + 1, n)


if __name__ == "__main__":
    func(1, 5)
