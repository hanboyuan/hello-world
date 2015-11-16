#!/usr/bin/env python
#-*- coding=utf-8 -*-
sum = 1
for i in range(1,121):
        #print i
        sum = sum * i
sum = str(sum)
len_num = len(sum)
num = 0
for i in range(1,100):
        print sum[len_num-i]
        #print type(sum[len_num-i])
        if sum[len_num-i] == '0':
                #print 'ok'
                num = num + 1
        else:
                break
print '#'*20
print num
