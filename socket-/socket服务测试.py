import asyncio
import socket
from concurrent.futures import ProcessPoolExecutor,ThreadPoolExecutor
import time

def block_way(x=None):
    sock = socket.socket()
    # sock.setblocking(False)
    sock.connect(('www.baidu.com',443))

    request = 'GET / HTTP/1.0\r\nHOST: example.com\r\n\r\n'.encode('ascii')

    sock.send(request)

    response = b''
    chunk = sock.recv(4096)
    while chunk:
        response+=chunk
        chunk = sock.recv(4096)

    return response


t = time.time()
# # #1 15s
# for i in range(1000):
#     print(i,block_way())
# print(time.time() - t)

# 2 1s
# with ThreadPoolExecutor() as ex:
#     results = ex.map(block_way,[x for x in range(10000)])
#     for i,r in enumerate(results):
#         print(i,r)
# print(time.time() - t)

#3 5s
# if __name__ == '__main__':
#     with ProcessPoolExecutor() as ex:
#         results = ex.map(block_way,[x for x in range(1000)])
#         for r in results:
#             print(r)
#     print(time.time()-t)

#4 1.7s
async def tcp_echo_client(i):
    reader, writer = await asyncio.open_connection(
        'www.baidu.com', 443)

    request = 'GET / HTTP/1.0\r\nHOST: example.com\r\n\r\n'.encode('ascii')
    writer.write(request)
    await writer.drain()

    data = await reader.read(100)
    print(f'Received:{i} {data.decode()!r}')

    # print('Close the connection')
    writer.close()
    # await writer.wait_closed()

async def main():
    tasks = []
    loop = asyncio.get_event_loop()
    for i in range(1000):
        #1 20s 为什么慢
        # await tcp_echo_client(i)

        #2 2s
        t = loop.create_task(tcp_echo_client(i))
        tasks.append(t)
    for t in tasks:
        await t

        #3 2s
    #     tasks.append(tcp_echo_client(i))
    # await asyncio.gather(*tasks)

asyncio.run(main())
print(time.time() - t)

