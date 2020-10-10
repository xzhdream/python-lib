import sys


class A():
    def __init__(self):
        '''初始化对象'''
        print('object born id:%s' % str(hex(id(self))))


def f1():
    '''循环引用变量与删除变量'''
    while True:
        c1 = A()
        del c1


def func(c):
    print('obejct refcount is: ', sys.getrefcount(c))  # getrefcount()方法用于返回对象的引用计数


if __name__ == '__main__':
    # 生成对象
    a = A()
    func(a)

    # 增加引用
    b = a
    func(a)

    # 销毁引用对象b
    del b
    func(a)

# 导致引用计数+1的情况
# 对象被创建，例如a=23
# 对象被引用，例如b=a
# 对象被作为参数，传入到一个函数中，例如func(a)
# 对象作为一个元素，存储在容器中，例如list1=[a,a]

# 导致引用计数-1的情况
# 对象的别名被显式销毁，例如del a
# 对象的别名被赋予新的对象，例如a=24
# 一个对象离开它的作用域，例如:func函数执行完毕时，func函数中的局部变量（全局变量不会）
# 对象所在的容器被销毁，或从容器中删除对象


