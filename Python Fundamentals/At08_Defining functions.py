import math

# 空函数
# 如果想定义一个什么事也不做的空函数，可以用pass语句：

def nop():
    pass

# 返回多个值

def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y - step * math.sin(angle)
    return nx, ny # 返回值是一个tuple
