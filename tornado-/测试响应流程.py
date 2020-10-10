import asyncio

from tornado.web import Application,RequestHandler

class MainPageHandler(RequestHandler):
    async def get(self):
        await self.finish({'1':1})
        await asyncio.sleep(2)
        print('---------')


app = Application([
        (r"/", MainPageHandler)
])
app.listen(port=8000)

asyncio.get_event_loop().run_forever()

