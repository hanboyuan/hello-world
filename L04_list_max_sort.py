#!/usr/bin/env python
#-*- coding=utf-8 -*-
###########################
Alist = [1,9,2]
def maxlist(list_2):
        num = len(list_2)
        if num != 0 :
                list_2.sort()
                print list_2[-1]
        else:
                pass
        #return max(aslit)
print maxlist(Alist)
