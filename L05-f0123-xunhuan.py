#!/usr/bin/env python
#-*- coding=utf-8 -*-
########################
def f(target):
    if target == 0 or target == 1:
        return 1
    else:
        first = 1
        second = 1
        for i in range(2,target+1):
            sum = first + second
            first = second
            second = sum
        return sum
print f(3)
