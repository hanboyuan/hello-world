#!/usr/bin/env python
#-*- coding=utf-8 -*-
num = 1
num_2 = 0
for i in range(1,121):
    num = num * i
while num%10 == 0 :
    num_2 = num_2 + 1
    num = num/10
print num_2
