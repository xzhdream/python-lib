import asyncio
import threading
import time


async def tcp_echo_client(i):
    reader, writer = await asyncio.open_connection(
        'www.baidu.com', 443)

    request = 'GET / HTTP/1.0\r\nHOST: example.com\r\n\r\n'.encode('ascii')
    writer.write(request)
    await writer.drain()

    data = await reader.read(100)
    print(f'Received:{i} {data.decode()!r}')

    print('Close the connection')
    writer.close()
    await writer.wait_closed()

def th_loop(loop):
    asyncio.set_event_loop(loop)
    loop.run_forever()

def main(loop):
    for i in range(10):
        #1 20s 为什么慢
        # await tcp_echo_client(i)
        f = asyncio.run_coroutine_threadsafe(tcp_echo_client(i),loop)
        fs.append(f)

fs = []
t = time.time()
loop = asyncio.get_event_loop()
th = threading.Thread(target=th_loop,args=(loop,))
th.start()

main(loop)


print(time.time() - t)

