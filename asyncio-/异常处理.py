import asyncio

async def bug():
    raise Exception("not consumed")

async def echo():
    await asyncio.sleep(2)
    print('---------')

async def main():
    asyncio.create_task(bug())
    await echo()

asyncio.run(main())