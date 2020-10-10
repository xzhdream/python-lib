import asyncio
import functools


async def run_df(loop):
    print('in run_df')

    cmd_done = asyncio.Future(loop=loop)
    factory = functools.partial(DFProtocol, cmd_done)
    proc = loop.subprocess_exec(
        factory,
        'df', '-hl',
        stdin=None,
        stderr=None,
    )
    try:
        print('launching process')
        transport, protocol = await proc
        print('waiting for process to complete')
        await cmd_done
    finally:
        transport.close()

    return cmd_done.result()

# 该类DFProtocol是从派生的 SubprocessProtocol，该类定义了用于通过管道与另一个进程进行通信的类的API。done参数应为Future，调用方将使用该参数来监视过程完成。
class DFProtocol(asyncio.SubprocessProtocol):

    FD_NAMES = ['stdin', 'stdout', 'stderr']

    def __init__(self, done_future):
        self.done = done_future
        self.buffer = bytearray()
        super().__init__()

    # 与套接字通信一样，connection_made()在建立新进程的输入通道时调用。该transport 参数是一个子类的实例 BaseSubprocessTransport。如果将流程配置为接收输入，则它可以读取流程输出的数据并将数据写入该流程的输入流。
    def connection_made(self, transport):
        print('process started {}'.format(transport.get_pid()))
        self.transport = transport

    # 进程生成输出后，pipe_data_received()将使用文件描述符调用该文件，在该文件描述符中发出数据并从管道读取实际数据。协议类将过程的标准输出通道的输出保存在缓冲区中，以供以后处理。
    def pipe_data_received(self, fd, data):
        print('read {} bytes from {}'.format(len(data),
                                             self.FD_NAMES[fd]))
        if fd == 1:
            self.buffer.extend(data)

    # 当进程终止时，process_exited()被调用。可以通过调用从传输对象获得进程的退出代码get_returncode()。在这种情况下，如果没有错误报告，则在通过Future实例返回之前，对可用输出进行解码和解析。如果有错误，则假定结果为空。设置future的结果将run_df()表明该进程已退出，因此它将清理并返回结果。
    def process_exited(self):
        print('process exited')
        return_code = self.transport.get_returncode()
        print('return code {}'.format(return_code))
        if not return_code:
            cmd_output = bytes(self.buffer).decode()
            results = self._parse_results(cmd_output)
        else:
            results = []
        self.done.set_result((return_code, results))

    # 命令输出被解析为字典序列，将标题名称映射到输出的每一行的值，并返回结果列表。
    def _parse_results(self, output):
        print('parsing results')
        # Output has one row of headers, all single words.  The
        # remaining rows are one per filesystem, with columns
        # matching the headers (assuming that none of the
        # mount points have whitespace in the names).
        if not output:
            return []
        lines = output.splitlines()
        headers = lines[0].split()
        devices = lines[1:]
        results = [
            dict(zip(headers, line.split()))
            for line in devices
        ]
        return results

# 使用run_df()来运行协程run_until_complete()，然后检查结果并打印每个设备上的可用空间。
event_loop = asyncio.get_event_loop()
try:
    return_code, results = event_loop.run_until_complete(
        run_df(event_loop)
    )
finally:
    event_loop.close()

if return_code:
    print('error exit {}'.format(return_code))
else:
    print('\nFree space:')
    for r in results:
        print('{Mounted:25}: {Avail}'.format(**r))