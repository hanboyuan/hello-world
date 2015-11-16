#!/usr/bin/env python
#-*- coding=utf-8 -*-
num = 1
for i in range(1,121):
    num = num * i
print num
num = str(num)
list_1 = list(num)
list_1.sort()
num = "".join(list_1)
print num
