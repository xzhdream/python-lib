from functools import partial
from threading import Thread


t = Thread(target=partial(print,'11111'))
t.start()

print(t.ident)
print(id(t))

t.join()