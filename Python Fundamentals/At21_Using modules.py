#!/usr/bin/env python3
# -*- coding: utf-8 -*-

' a test module '

__author__ = 'Michael Liao'

import sys  # 导入sys模块

# sys模块有一个argv变量，用list存储了命令行的所有参数。
# argv至少有一个元素，因为第一个参数永远是该.py文件的名称.
def test():
    args = sys.argv
    if len(args)==1:
        print('Hello, world!')
    elif len(args)==2:
        print('Hello, %s!' % args[1])
    else:
        print('Too many arguments!')


# 作用域
# 正常的函数和变量名是公开的（public），
# 可以被直接引用，比如：abc，x123，PI等；
# 类似__xxx__这样的变量是特殊变量，可以被直接引用，但是有特殊用途.
# 类似_xxx和__xxx这样的函数或变量就是非公开的（private），
# 不应该被直接引用，比如_abc，__abc等；









# 当我们在命令行运行hello模块文件时，
# Python解释器把一个特殊变量__name__置为__main__，
# 而如果在其他地方导入该hello模块时，if判断将失败，
# 因此，这种if测试可以让一个模块通过命令行运行时执行一些额外的代码，
# 最常见的就是运行测试。
if __name__=='__main__':
    test()
