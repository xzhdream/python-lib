import sys


class A:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls,'instance'):
            cls.instance = super().__new__(cls)
        return cls.instance

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
        c = A()
        c1=A()
        func(c1)

        c2=A()
        func(c2)

        c1.t=c2
        func(c1)

        c2.t=c1
        func(c2)

        del c1

        del c2

        func(c)
        if count>0:
            break
        print('-------------')

f2()


