# 操作文件和目录
import os
# 查看当前目录的绝对路径
print(os.path.abspath('.'))
# 在某个目录下创建一个新目录，首先把新目录的完整路径表示出来:
newpath = os.path.join(os.path.abspath('.'), 'testdir')
os.mkdir(newpath)
os.rmdir(newpath)
print(os.path.split('/Users/michael/testdir/file.txt'))
# os.path.splitext()可以直接让你得到文件扩展名，很多时候非常方便：
print(os.path.splitext('/path/to/file.txt'))
# 对文件重命名:
# os.rename('test.txt', 'test.py')

match_files = []
exp = ''


def find(exp, curdir):
    for x in os.listdir(curdir):
        new_path = os.path.join(curdir, x)
        if os.path.isfile(new_path):
            file_name = os.path.split(new_path)[1]
            if file_name.find(exp) != -1:
                match_files.append(new_path)
            print('file', new_path)
        elif os.path.isdir(new_path):
            print('dir', new_path)
            find(exp, new_path)

find('dog','./test')
print(match_files)

