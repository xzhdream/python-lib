import asyncio
import sys

async def get_date():
    code = 'import datetime; print(datetime.datetime.now())'

    # Create the subprocess; redirect the standard output
    # into a pipe.
    print('333333')
    proc = await asyncio.create_subprocess_exec(
        sys.executable, '-c', code,
        stdout=asyncio.subprocess.PIPE)

    # Read one line of output.
    data = await proc.stdout.readline()
    line = data.decode('ascii').rstrip()

    # Wait for the subprocess exit.
    await proc.wait()
    print(f'333333-{line}')
    return line

async def a():
    print('1111')
    await asyncio.sleep(1)
    print('1111-')

async def b():
    print('2222')
    await asyncio.sleep(4)

    print('2222-')


tasks = asyncio.gather(get_date(),a(),b())
date = asyncio.get_event_loop().run_until_complete(tasks)
print(f"Current date: {date}")