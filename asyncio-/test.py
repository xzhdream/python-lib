import asyncio

class Future:

    def __init__(self, loop):
        self.loop = loop
        self.done = False
        self.result = None
        self.co = None

    def set_coroutine(self, co):
        self.co = co

    def set_result(self, result):
        self.done = True
        self.result = result

        if self.co:
            self.loop.add_coroutine(self.co)

    def __await__(self):
        if not self.done:
            yield self
        return self.result

async def main(loop):
    f = Future(loop)
    await f

loop=asyncio.get_event_loop()
loop.run_until_complete(main(loop))


