# def consumer():
#     r = ''
#     while True:
#         n = yield r
#         if not n:
#             return
#         print('[CONSUMER] Consuming %s...' % n)
#         r = '200 OK'
#
# def produce(c):
#     c.send(None)
#     n = 0
#     while n < 5:
#         n = n + 1
#         print('[PRODUCER] Producing %s...' % n)
#         r = c.send(n)
#         print('[PRODUCER] Consumer return: %s' % r)
#     c.close()
#
# c = consumer()
# produce(c)


# def printer():
#     counter = 0
#     while True:
#         string = (yield)
#         print('{0} {1}'.format(counter, string))
#         counter += 1
#
#
# if __name__ == '__main__':
#     p = printer()
#     next(p)
#     p.send('Hi')
#     p.send('My name is yangliu.')
#     p.send('Bye')

def task(name, times):
    for i in range(times):
        yield
        print(name, i)

from collections import deque
class Runner(object):
    def __init__(self, tasks):
        self.tasks=deque(tasks)

    def next(self):
        return self.tasks.pop()

    def run(self):
        while len(self.tasks):
            task = self.next()
            try:
                next(task)
            except StopIteration:
                pass
            else:



