import asyncio

async def _a():
    return 1

async def a():
    print('1')
    await _a()
    return 11


x = a()
y = x.send(None)

