import asyncio


async def test(x):
    await asyncio.sleep(0.5)
    print(x)

async def main0(x,y):
    asyncio.ensure_future(test(y))
    print(x)

async def main1():
    await main0('x00000000','x11111111')
    print('----x----')
    await asyncio.sleep(1)

async def main2():
    asyncio.ensure_future(main0('y00000000','y11111111'))
    print('----y----')
    await asyncio.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.gather(main2(),main1()))
