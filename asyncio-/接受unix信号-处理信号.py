import asyncio
import functools
import os
import signal


def signal_handler(name):
    print('signal_handler({!r})\n'.format(name))

# 信号处理程序使用进行注册 add_signal_handler()。
# 第一个参数是信号，第二个参数是回调。
# 回调不传递任何参数，因此如果需要参数，则可以使用来包装函数 functools.partial()。
event_loop = asyncio.get_event_loop()

event_loop.add_signal_handler(
    signal.SIGHUP,
    functools.partial(signal_handler, name='SIGHUP'),
)
event_loop.add_signal_handler(
    signal.SIGUSR1,
    functools.partial(signal_handler, name='SIGUSR1'),
)
event_loop.add_signal_handler(
    signal.SIGINT,
    functools.partial(signal_handler, name='SIGINT'),
)


# 此示例程序使用协程通过来向自身发送信号 os.kill()。
# 发送每个信号后，协程会产生控制权以允许处理程序运行。
# 在正常的应用程序中，会有更多的地方使应用程序代码回落到事件循环，而无需像这样的人为地产生。
async def send_signals():
    pid = os.getpid()
    print('starting send_signals for {}\n'.format(pid))

    for name in ['SIGHUP', 'SIGHUP', 'SIGUSR1', 'SIGINT']:
        print('sending {}'.format(name))
        os.kill(pid, getattr(signal, name))
        # Yield control to allow the signal handler to run,
        # since the signal does not interrupt the program
        # flow otherwise.
        print(f'yielding control {name}')
        await asyncio.sleep(0.01)
    return

# 主程序运行，send_signals()直到发送完所有信号为止。
try:
    event_loop.run_until_complete(send_signals())
finally:
    event_loop.close()