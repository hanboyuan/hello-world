#!/usr/bin/env python
#-*- coding=utf-8 -*-
########################
def f(target):
    if target == 0 or target == 1:
        return 1
    else:
        return f(target-1) + f(target -2)
print f(3)
