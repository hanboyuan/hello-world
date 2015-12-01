#!/usr/bin/env python
#-*- coding=utf-8 -*-
###########################
Alist = [1,9,2]
def maxlist(list_2):
        num = len(list_2)
        if num != 0 :
                max_value = list_2[0]
                for k in list_2:
                        if k >= max_value:
                                max_value = k
                        else:
                                pass
                return max_value
        else:
                pass
        #return max(aslit)
print maxlist(Alist)
