import asyncio
import asyncio.subprocess


async def to_upper(input):
    print('in to_upper')

    create = asyncio.create_subprocess_exec(
        'tr', '[:lower:]', '[:upper:]',
        stdout=asyncio.subprocess.PIPE,
        stdin=asyncio.subprocess.PIPE,
    )
    print('launching process')
    proc = await create
    print('pid {}'.format(proc.pid))

    # to_upper()使用的communicate()方法 Process将输入字符串发送到命令并异步读取所有结果输出。与subprocess.Popen相同方法的 版本一样， communicate()返回完整的输出字节字符串。如果命令是可能产生的数据量超出可舒适到存储器，输入不能生产一次全部，或输出必须增量处理，可以使用标准输入，stdout和stderr的把手Process，而不是直接召唤 communicate()。
    print('communicating with process')
    stdout, stderr = await proc.communicate(input.encode())

    # I / O完成后，等待进程完全退出以确保正确清理了该进程。
    print('waiting for process to complete')
    await proc.wait()

    # 然后可以检查返回码，并对输出字节字符串进行解码，以从协程准备返回值。
    return_code = proc.returncode
    print('return code {}'.format(return_code))
    if not return_code:
        results = bytes(stdout).decode()
    else:
        results = ''

    return (return_code, results)

# 该程序的主要部分建立一个要转换的消息字符串，然后设置事件循环以运行to_upper() 并打印结果。
MESSAGE = """
This message will be converted
to all caps.
"""

event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
        to_upper(MESSAGE)
    )
finally:
    event_loop.close()

if return_code:
    print('error exit {}'.format(return_code))
else:
    print('Original: {!r}'.format(MESSAGE))
    print('Changed : {!r}'.format(results))