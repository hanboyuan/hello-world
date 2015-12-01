#!/usr/bin/env python
#-*- coding=utf-8 -*-
########################
def f(target):
    if target == 1:
        return 1
    elif target > 1:
        return str(f(target-1))+str(target)
    else:
        raise ValueError('bad args')
####################################
print f(3)
