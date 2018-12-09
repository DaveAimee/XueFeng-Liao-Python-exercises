from io import StringIO
from io import BytesIO
# StingIO
f = StringIO()
num1=f.write('hello')
num2=f.write(' ')
num3=f.write('world!')
print(num1)
print(num2)
print(num3)
print(f.getvalue())
f2 = StringIO('Hello!\nHi!\nGoodbye!')
while s != '':
    s = f2.readline()
    print(s.strip())

# BytesIO
f = BytesIO()
f.write('中文'.encode('utf-8'))