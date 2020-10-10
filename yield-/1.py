import time

def consumer():
    r = ""
    while True:
        n = yield r
        if not n:
            return
        print("consumer %s"%n)
        r = "200 OK"

def producer(c):
    x = c.__next__()
    # next(c)
    # c.send(None)

    n = 0
    while n < 3:
        n = n + 1
        print("producer %s"%n)
        r = c.send(n)
        print("producer return %s\n"%r)
    c.close()

if __name__ == "__main__":
    c = consumer()
    producer(c)