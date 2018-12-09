# ASCII: 使用一个字节表示字符。
# Unicode: 大多使用两个字节表示一个字符。
# UTF-8: 采用变长编码。与ASCII编码兼容

# Python的字符串
print('包含中文的str')
ord('A')  # 获取字符的整数表示
ord('中')
chr(66)  # 把编码转换为具体的字符

# 由于Python的字符串类型是str，在内存中以Unicode表示，一个字符对应若干个字节。
# 如果要在网络上传输，或者保存到磁盘上，就需要把str变为以字节为单位的bytes。
# Python对bytes类型的数据用带b前缀的单引号或双引号表示：
# 例如: x = b'ABC'
# 以Unicode表示的str通过encode()方法可以编码为指定的bytes，例如
'ABC'.encode('ascii')
'中文'.encode('utf-8')

# 要把bytes变为str，就需要用decode()方法：
b'ABC'.decode('ascii')

# 格式化输出
print("Hi, %s, you have $%d" % ('YangLiu', 1000))


