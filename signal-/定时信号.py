import signal
import threading
# Define signal handler function
import time


def myHandler(signum, frame):
    print("Now, it's the time ",threading.get_ident())
    # exit()

# register signal.SIGALRM's handler
signal.signal(signal.SIGALRM, myHandler)   #注册信号进行函数处理，若未注册，则触发默认处理杀死进程
signal.alarm(5)

handler = signal.getsignal(signal.SIGALRM)
print(handler)

while True:
    time.sleep(1)
    print('not yet ',threading.get_ident())

