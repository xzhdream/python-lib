def fun_inner():
    i = 10
    while True:
        i = yield i

def fun_outer():
    a = 0
    b = 1
    inner = fun_inner()
    x = inner.send(None)
    while True:
        a = inner.send(b)
        b = yield a

if __name__ == '__main__':
    outer = fun_outer()
    y = outer.send(None)
    for i in range(5):
        print(outer.send(i))