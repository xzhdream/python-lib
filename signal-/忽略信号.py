import signal, time

def a(signum, frame):
    print(signum,'xxxxx')

# 3秒后终止程序
signal.signal(signal.SIGALRM,a)
signal.alarm(5)
# 当遇到SIGINT即CTRL+C时忽略SIG_IGN
signal.signal(signal.SIGINT, signal.SIG_IGN)
# 阻塞等待信号的发生，无论什么信号都可以。
signal.pause()