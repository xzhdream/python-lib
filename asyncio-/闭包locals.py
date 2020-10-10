import asyncio
import collections


async def a():
    tt = 1
    print('a1:',locals())
    await asyncio.sleep(1)
    print('a2:',locals())


async def b():
    tt = 2
    print('b1:',locals())
    del tt
    print('b2:',locals())
    c()

def c():
    print('c1:',locals())
    t = {'1':1}
    q = collections.deque()
    q.append(t)
    del t
    print('c2:',q,len(q))

asyncio.get_event_loop().run_until_complete(asyncio.gather(a(),b()))