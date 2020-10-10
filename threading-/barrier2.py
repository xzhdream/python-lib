import threading, logging

logging.basicConfig(level=logging.INFO, format="[-] %(threadName)s %(message)s")


def work(barrier: threading.Barrier):
    logging.info("n_waiting = {} count={}".format(barrier.n_waiting,barrier._count))
    try:
        bid = barrier.wait()
        logging.info("after barrier {}".format(bid))
    except threading.BrokenBarrierError:
        logging.info("Broken Barrier in {}".format(threading.current_thread()))


barrier = threading.Barrier(3)

for x in range(1, 12):  # 12个
    if x == 3:
        barrier.abort()  # 有一个人坏了规矩
    elif x == 6:
        barrier.reset()
    threading.Event().wait(1)
    threading.Thread(target=work, args=(barrier,), name="Barrier-{}".format(x)).start()
