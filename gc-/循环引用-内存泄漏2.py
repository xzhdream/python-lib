import sys


class A:
    def __init__(self):
        '''初始化对象'''
        print('object born id:%s' % str(hex(id(self))))

def func(c):
    print('obejct refcount is: ', sys.getrefcount(c))  # getrefcount()方法用于返回对象的引用计数


def f2():
    '''循环引用'''
    count=0
    while True:
        count+=1
        c1=A()
        c11 = c1
        func(c1)
        c2=A()
        c22=c2
        func(c2)

        c1.t=c2
        func(c2)
        c2.t=c1
        func(c1)

        del c1
        del c2

        func(c11)
        func(c22)

        if count>0:
            break
        print('-------------')

f2()


