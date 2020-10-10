import asyncio
import time


async def a():
    await asyncio.sleep(2)
    print('a'*10,time.time())

async def b():
    await asyncio.sleep(2)
    print('b'*10,time.time())

async def main():
    print(f'{"*"*3}main{"*"*3}',time.time())
    await a()
    await b()

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

# output:
# ***main*** 1599636621.3141491
# aaaaaaaaaa 1599636623.315339
# bbbbbbbbbb 1599636625.3188338

#总结：
#main 进入了io loop进行调度，而 a,b 函数仅是在main中顺序执行

# await只是yield 的另类封装，所以如果要并发执行，而不是串行等待一个完成，再运行另一个的话，
# 需要通过create_task或者enture_future进行任务封装，使其进入到ioloop内部进行调度。

#问题：
#ioloop调度是如何进行读写非阻塞的？
#通过select，还是其他

