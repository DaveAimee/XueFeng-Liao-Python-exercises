import psutil
# 获取CPU信息
print('CPU logical core: %d', psutil.cpu_count())
print('CPU physicle core: %d', psutil.cpu_count(logical = False))
print(psutil.disk_partitions())