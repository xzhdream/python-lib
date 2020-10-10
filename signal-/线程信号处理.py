import time
import os
import signal
import threading

receive_times = 0

def handler(signalnum, frame):
    global receive_times
    print (u"收到信号", signalnum, frame, receive_times)
    receive_times += 1
    if receive_times > 3:
        # os.kill(os.getpid(), signal.SIGTERM) # 我疯起来连自己都杀
        exit(0)

def run():
    print ("thread %s run:"%(threading.currentThread().getName()))
    time.sleep(10)
    print ("thread %s done"%(threading.currentThread().getName()))

def main():
    print ("pid:", os.getpid())
    signal.signal(signal.SIGINT, handler)

    thread_list = []
    for i in range(5):
        thread = threading.Thread(target = run)
        thread_list.append(thread)

    for thread in thread_list:
        thread.start()

    for thread in thread_list:
        thread.join()

    print ("all thread done")

main()