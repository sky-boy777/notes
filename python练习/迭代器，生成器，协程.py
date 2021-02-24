# class A:
#     def __init__(self, num):
#         self.num = num
#         self.x = 0
#         self.y = 1
#
#     def __iter__(self):  # 必须：定义了__iter__()后成可迭代对象
#         return self   # 返回一个可迭代对象（因为定义了__iter__()所以本身就是可迭代对象）
#
#     def __next__(self):  # 再定义__next__()方法后成为迭代器
#         if self.x > self.num:
#             raise StopIteration
#         self.x, self.y = self.y, self.x + self.y
#         return self.x
#
#
# a = A(10)  # 实例成为一个可迭代对象
# for i in a:  # 使用for...i会调用__next__()方法，返回值i为__next__()的返回值
#     print(i)
#
# # 第二种使用方法
# s = list(A(10))
# print(s)


# 定义了yield的函数称为生成器对象（一种特殊的迭代器）
# def fun(num):
#     '''生成器应用：斐波那契数列'''
#     c = 0
#     d = 1
#     while c < num:
#         flag = yield c  # 返回c后暂停，下次再调用会从下一行执行：c, d = d, c + d
#         print(flag)
#         c, d = d, c + d
#
#
# m = fun(10)  # m为生成器对象，不会调用fun（）
# for j in m:
#     m.send('a')
#     print(j)



# 生成器实现并发（交替执行）,协程
# def t1():
#     while 1:
#         print('1111111')
#         yield
#
#
# def t2():
#     while 1:
#         print('2222222')
#         yield
#
#
# test1 = t1()
# test2 = t2()
# while 1:
#     next(test1)
#     next(test2)

import time
import gevent  # 协程：当一个任务需要耗时
from gevent import monkey  # 补丁

monkey.patch_all()  # 将耗时的代码转自动换成gevent.sleep()，比如time.sleep()

def t1(a):
    while 1:
        print(a)
        time.sleep(1)  # 会自动转换成gevent.sleep(1)


def t2(b):
    while 1:
        print(b)
        time.sleep(1)


gevent.joinall([  # 阻塞主线程，等待协程结束
    # 遇到耗时自动切换任务t1,t2切换
    gevent.spawn(t1, '111'),
    gevent.spawn(t2, '222')
])

# g1 = gevent.spawn(t1)
# g2 = gevent.spawn(t2)
# g1.join()  # 阻塞主线程
# g2.join()  # 阻塞主线程
