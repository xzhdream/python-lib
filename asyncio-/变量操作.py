import asyncio
import threading

async def test(a):
    await asyncio.sleep(1)
    print('--0',id(a),a)

async def main():
    a = {'1':[1,2,3,4,5]}
    print('-x-',locals())

    asyncio.ensure_future(test(a))
    print('==1',id(a),a)
    del a
    print('-y-',locals())
    await asyncio.sleep(3)

asyncio.get_event_loop().run_until_complete(main())
