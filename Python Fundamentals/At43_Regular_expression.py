import re
print(re.match(r'[a-zA-Z\.]+@[a-zA-Z]+\.com$','bob#example.com'))
m=re.match(r'<([a-zA-Z\s]+)>\s*[a-zA-Z]+@[a-zA-Z]+\.[a-zA-Z]+$','<Tom Paris> tom@voyager.org')
print(m.groups())