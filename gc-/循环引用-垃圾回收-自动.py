import gc
import sys
import time


class A:
    def __init__(self):
        '''初始化对象'''
        print('object born id:%s' % str(hex(id(self))))

def func(c):
    print('obejct refcount is: ', sys.getrefcount(c))  # getrefcount()方法用于返回对象的引用计数


def f4():
    '''垃圾自动回收'''
    print(gc.get_count())     #回收计数
    # print(gc.get_objects()) #收集器所追踪的所有对象列表
    print(gc.get_stats())     #回收统计
    print(gc.get_threshold()) #回收阈值


    a=A()
    print(gc.get_count())
    # print(gc.get_objects())
    print(gc.get_stats())
    print(gc.get_threshold())


    del a
    print(gc.get_count())
    # print(gc.get_objects())
    print(gc.get_stats())
    print(gc.get_threshold())
    print(gc.get_freeze_count())




f4()