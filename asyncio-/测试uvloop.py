import asyncio
import uvloop

async def main():
    print('111')

asyncio.set_event_loop_policy(uvloop.EventLoopPolicy())
asyncio.get_event_loop().run_until_complete(main())
