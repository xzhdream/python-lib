import asyncio
import collections
import gc
import sys

q = collections.deque()

async def test(x):
    await asyncio.sleep(1)
    print('-',x,id(x))
    print(sys.getrefcount(x))


async def main():
    # 初始化临时消息队列
    temp_question_queue = [111,222]
    print(id(temp_question_queue))

    asyncio.ensure_future(test(temp_question_queue))
    del temp_question_queue
    print('--',locals())
    await asyncio.sleep(1)



asyncio.get_event_loop().run_until_complete(main())





