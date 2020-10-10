import signal
# Define signal handler function
def myHandler(signum, frame):
    print('I received: ', signum,frame)

# register signal.SIGTSTP's handler
signal.signal(signal.SIGTSTP, myHandler)
signal.pause()
print('End of Signal Demo')
# 有问题待测试

#触发
# kill -SIGTSTP 79694


