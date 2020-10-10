# 导入线程模块
import threading
import time


def plyer_display():
    print('初始化通过完成，音视频同步完成，可以开始播放....')


# 设置3个障碍对象
barrier = threading.Barrier(3, action=plyer_display, timeout=None)


def player_init(statu):
    while True:
        print(statu)
        time.sleep(1)
        try:
            # 设置超时时间，如果2秒内，没有达到障碍线程数量，
            # 会进入断开状态，引发BrokenBarrierError错误
            barrier.wait(2)
        except Exception as e:  # 断开状态，引发BrokenBarrierError错误
            # print("断开状态... ")
            continue
        else:
            print("xxxooyyyxxxooyyyxxxooyyy")
            break


if __name__ == '__main__':
    statu_list = ["init ready", "video ready", "audio ready"]
    thread_list = list()
    for i in range(0, 3):
        t = threading.Thread(target=player_init, args=(statu_list[i],))
        t.start()

        time.sleep(0.01)
        thread_list.append(t)
        if i == 1:  # 重置状态
            print("不想看爱情片，我要看爱情动作片....")
            barrier.reset()
    for t in thread_list:
        t.join()