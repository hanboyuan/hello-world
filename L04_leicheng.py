#!/usr/bin/env python
#-*- coding=utf-8 -*-
###########################
def func(n):
 num = 1
 for i in range(1,n+1):
  num = num * i
 return num
print func(3)
