def fun_inner():
    i = 0
    while True:
        i = yield i


def fun_outer():
    yield from fun_inner()


if __name__ == '__main__':
    outer = fun_outer()
    outer.send(None)
    for i in range(5):
        print(outer.send(i))