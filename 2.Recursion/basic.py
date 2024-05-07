count = 5


def func():
    global count
    if count == 0:
        return
    print(count)
    count -= 1
    func()


if __name__ == "__main__":
    func()
