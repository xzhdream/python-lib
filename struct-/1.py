from struct import *
print(pack('hhl', 1, 2, 3))
print(unpack('hhl', b'\x01\x00\x02\x00\x00\x00\x00\x00\x03\x00\x00\x00\x00\x00\x00\x00'))
print(calcsize('hhl'))
print(calcsize('hhl'))

print(pack('ci', b'*', 0x12131415))
print(pack('ic', 0x12131415, b'*'))
print(calcsize('ci'))
print(calcsize('ic'))