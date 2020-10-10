import signal, time

# 3秒后终止程序
print(signal.alarm(3)) # output:0
time.sleep(1)
print(signal.alarm(3)) # output:2

# 捕获信号，使程序继续进行
signal.signal(signal.SIGALRM,lambda x,y:print('1'))

# 阻塞等待信号的发生，无论什么信号都可以。
signal.pause()

while True:
    time.sleep(1)
    print("working")