import os
import time
import selectors

r,w = os.pipe()

sel = selectors.KqueueSelector()
sel.register(r,selectors.EVENT_READ)

t = time.time()
while True:
    ready = sel.select(timeout=1)
    print('ready:', ready)
    if ready:
        x = os.read(r,length)
        print(x)
        break
    elif time.time() - t >10:
        length = os.write(w,b'1234')
        print('write:',length)
    else:
        print('timeout:',time.time()-t)


