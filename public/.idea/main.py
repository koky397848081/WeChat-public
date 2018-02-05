# -*- coding: UTF-8 -*-

import time;  # 引入time模块
import sys;
ticks = time.time()
# print "当前时间戳为:", ticks

'''
这里是多行注释
循环
'''

'''
for letter in 'Python':
    if letter == 'h':
        continue
    print  '当前字母：',letter
'''
#输入
'''
birth = raw
'''
birth = int(raw_input('brith =:'))
if birth < 2000:
    print '00前'
else:
    print "00后"


x = 'runoob';
#sys.stdout.write('\n' + x )
#截取字符串   [头下标:尾下标]
print x[1:2] #输出为u

if 1:
    a = b = 6
elif angel:
    a = 5
else:
    a = 9
# print "\n" + "a =" ,a

print sys.argv

#循环
'''
sum = 0
for x in range(101):
    sum = sum + x
#print sum

'''

sum = 0
n = 100
while n > 0:
    sum = sum + n
    n -= 1
print sum