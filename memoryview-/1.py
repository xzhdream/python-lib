a = 'aaaaaa'
b = a[:2]
print('1:',b)
print('*********')

a = bytearray('aaaaaa'.encode())
b = a[:2]
print('2:',b)
b[:2] = b'bb'
print('3:',a)
print('4:',b)
print('*********')

a = memoryview('aaaaaa'.encode())
print(a.readonly)
b = a[:2]
print('5:',a.tobytes())
print('6:',b.tobytes())
print('*********')

a = memoryview(bytearray('aaaaaa'.encode()))
print(a.readonly)
b = a[:2]
print('7:',b.tobytes())
b[:2] = b'bb'
print('8:',a.tobytes())
print('9:',b.tobytes())