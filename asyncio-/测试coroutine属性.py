import asyncio
import collections
import types

_COROUTINE_TYPES = (types.CoroutineType, types.GeneratorType,
                    collections.abc.Coroutine)


async def a():
    print('xxxx')

def b():
    pass

async def main():
    # 测试coroutine
    t = a()
    for x in _COROUTINE_TYPES:
        print('-',x)
        if isinstance(t,x):
            print(t,x)

    # 测试普通函数
    for x in _COROUTINE_TYPES:
        print('-', x)
        if isinstance(b, x):
            print(b, x)

    await t

asyncio.run(main())
