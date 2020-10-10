import time
import asyncio
from  threading import Thread

now = lambda: time.time()


def start_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()


async def do_some_work(x):
    print(f'Waiting {x}')
    await asyncio.sleep(x)
    print(f'Done after {x}s')


def more_work(x):
    print(f'More work {x}')
    time.sleep(x)
    print('Finished more work {x}')


start = now()
# 主线程中创建一个 new_loop
new_loop = asyncio.get_event_loop()
# 创建子线程 在其中开启无限事件循环
t = Thread(target=start_loop, args=(new_loop,))
t.start()
print(f'TIME: {time.time() - start}')

# 在主线程中新注册协程对象
# 这样即可在子线程中进行事件循环的并发操作 同时主线程又不会被 block
# 一共执行的时间大概在 6 s 左右
asyncio.run_coroutine_threadsafe(do_some_work(6), new_loop)
asyncio.run_coroutine_threadsafe(do_some_work(4), new_loop)