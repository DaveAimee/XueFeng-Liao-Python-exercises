# namedtuple
from collections import namedtuple
Point = namedtuple('Point', ['x', 'y'])
p = Point(1, 2)
print(p.x)
print(p.y)

# deque
from collections import deque
q = deque(['a', 'b', 'c'])
q.append('x')
q.appendleft('y')
print(q)

# defaultdict
from collections import defaultdict
dd = defaultdict(lambda: 'N/A')
dd['key1'] = 'abc'
print(dd['key1'])
print(dd['not-found'])

# OrderedDict
from collections import OrderedDict
d = dict([('a',1), ('b',2), ('c', 3)])
print(d)
od = OrderedDict([('a',1), ('b',2), ('c', 3)])
print(od)
