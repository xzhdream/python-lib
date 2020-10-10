import asyncio
from threading import Thread,current_thread


async def create_task(event_loop):
    print(f'create{current_thread().ident}')
    i = 0
    while True:
        # 每秒产生一个任务, 提交到线程里的循环中, event_loop作为参数
        asyncio.run_coroutine_threadsafe(production(i), event_loop)
        await asyncio.sleep(1)
        i += 1


async def production(i):
    # while True:
    print(f"第{i}个coroutine任务 thid{current_thread().ident}")
    await asyncio.sleep(5)


def start_loop(loop):
    #  运行事件循环， loop作为参数
    print(f'start{current_thread().ident}')
    asyncio.set_event_loop(loop)
    loop.run_forever()


thread_loop = asyncio.new_event_loop()  # 创建事件循环
print(id(thread_loop))
run_loop_thread = Thread(target=start_loop, args=(thread_loop,))  # 新起线程运行事件循环, 防止阻塞主线程
run_loop_thread.start()  # 运行线程，即运行协程事件循环

main_loop = asyncio.new_event_loop()
print(id(main_loop))
main_loop.run_until_complete(create_task(thread_loop))  # 主线程负责create coroutine object