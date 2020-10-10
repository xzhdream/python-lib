import mmap
import os

mm = mmap.mmap(-1, 13)
mm.write(b"Hello world!")

pid = os.fork()

if pid == 0:  # In a child process
    print(len(mm))

    mm.seek(0)
    mm[1:] = b'Gello world!'

    print(mm.readline())
    mm.close()