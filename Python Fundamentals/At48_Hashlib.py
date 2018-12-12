import hashlib

md5 = hashlib.md5()
md5.update('how to use md5 in python hashlib?'.encode('utf-8'))
print(md5.hexdigest())

def login(user, password):
    md5 = hashlib.md5()
    md5.update(password.encode('utf-8'))
    if md5.hexdigest() == db[user]:
        return True
    else:
        return False